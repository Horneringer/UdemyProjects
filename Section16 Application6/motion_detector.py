"""Питон включает камеру и начинается запись видео, в цикле считываются каждый кадр, отображается в командной строке
в виде массива, цвет кадра меняется на серый, далее повляется окно с кадром, кадры сменяют друг друга через указанный
промежуток времени, по нажатию клавиши q происходит выход из цикла, видео завершается, окна закрываются
"""

import cv2
import time
from datetime import datetime
import pandas

# переменная для хранения первого кадра, по умолчанию в ней ничего нет - None

first_frame = None


# список, где храниться статус; в начальный момент времени список пуст, обозначим первые два элементы None,
# чтобы избежать ошибки выхода за пределы массива

status_list = [None, None]

times = []

# создание датафрейма с двумя колонками - момент появления и исчезновения объекта

df = pandas.DataFrame(columns=['Start', 'End'])

# запускает захват видео объекта; в параметры передаём либо путь к видео файлу,
# либо цифры (0,1,2,3....), которые означают индекс записывающей в реальном времени камеры

video = cv2.VideoCapture(0)


# используем цикл для считывания каждого кадра видео

while True:
    # check - логическая переменная проверяет записывается видео или нет, frame - масив Numpy
    
    check, frame = video.read()

    # status обозначает отсутствие(0) или наличие(1) объекта в кадре
    
    status = 0

    # конвертация цвета в серый
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    gray = cv2.GaussianBlur(gray, (21, 21), 0)  # применение Гауссовского размытия к изображению; убирает шумы и
    # увеличивает точность вычисления разницы изображений; в параметрах размываемое изображение, картеж с шириной и
    # высотой матрицы размытия и коэффициент нормирования, для того чтобы средняя интенсивность оставалась не
    # изменой(div)
    
    if first_frame is None:  # если True,в first_frame записывается первый серый кадр и возврат к началу цикла после
        # continue, на второй итерации условие не выполняется и просто пропускается блок if
        first_frame = gray
        continue

    # вычисление абсолютной разницы между первым кадром(background'ом) и текущим
    
    delta_frame = cv2.absdiff(first_frame, gray)

    # устанавливаем порог; в delta_frame все пиксели с интенсивностью больше 30 отображаются белым(в интенсивности
    # 255), выбираем тип порога(бинарный), данный тип возвращает картеж с двумя значениями, второе значение -
    # обработанный кадр, к нему и получаем доступ через индекс
    
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    # метод морфологического расширения изображения(фильтр дилации); в параметре kernel передаём None, будет два
    # прохода по каждому кадру
    
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # поиск контуров всех выделенных объектов
    (_, cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:  # проверяем по очереди области внутри всех найденных контуров,
        if cv2.contourArea(contour) < 10000:  # если количество пикселей в области больше 10000
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)  # то захватываем её в прямоугольник, координаты верхнего левого
        # угла, ширину и высоту возвращает метод и они хранятся в соответствующих переменных

        # отображение прямоугольника по координатам, выбор цвета и толщины линии(захватывается изображение в RGB)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # добавление в список очередного статуса
    status_list.append(status)

    # два последних статуса в списке
    status_list = status_list[-2:]
    
    if status_list[-1] == 1 and status_list[-2] == 0:  # проверка 2х последних значений статуса; смена статуса с 0 на
        #  1 - появление объекта
        
        times.append(datetime.now())  # добавляем в список дату и время изменения статуса
    
    if status_list[-1] == 0 and status_list[-2] == 1:  # смена статуса с 1 на 0 - исчезновение объекта
        times.append(datetime.now())
    
    cv2.imshow('Gray Frame', gray)  # текущее серое изображение
    cv2.imshow('Delta', delta_frame)  # отображение разницы
    cv2.imshow('Thresh Frame', thresh_frame)  # отображение разницы с установленным порогом
    cv2.imshow('Color Frame', frame)
    
    key = cv2.waitKey(1)  # ставим время задержки скрипта перед началом следующей итерации(если оставить 0,
    # то по нажатию) количество секунд храним в переенной
    #  клавиши программа прекратит работу) time sleep больше не нужен
    
    if (key == ord('q')) or (key == ord('й')):  # метод ord позволяет считывать нажатую клавишу и выполнять условие
        if status == 1:  # проверка статуса перед выходом
            times.append(datetime.now())
        break

print(status_list)
print(times)

# проходим по всему списку times с шагом 2
for i in range(0, len(times), 2):
    
    # берется пара значений списка times, первое значение закидывается в колонку Start, второе - в End
    df = df.append({'Start': times[i], 'End': times[i + 1]}, ignore_index=True)

# создаём файл csv с нашим датафреймом
df.to_csv('Times.csv')

video.release()

cv2.destroyAllWindows()