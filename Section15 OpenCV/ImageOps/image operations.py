import cv2

img = cv2.imread('galaxy.jpg', 0)  # в параметры передаём единицу, если хотим прочитать файл в RGB и 0, если хотим
# прочитать в оттенках серого

print(img)  # содержимым переменной img является многомерный массив; числа означают интенсивность пикселей в оттенках
#  серого(см шкалу)

print(img.shape)  # размерность матрицы

print(img.ndim)  # размерность

resized_image = cv2.resize(img, (int(img.shape[0]/2), int(img.shape[1]/2)))  # меняем размер изображения; это можно сделать
# напрямую, указав новый размер, а можно получить доступ к элементам через img.shape, где [0]-первый элемент
# размерного картежа, [1] - второй элемент

print(resized_image.shape) # новый размер
cv2.imshow('Galaxy', resized_image)  # отображение окна с изображением файла; первый параметр - заголовок окна,
# второй - сам файл
cv2.imwrite('Galaxy_resized.jpg', resized_image)
cv2.waitKey(0)  # определяет каким способом закрыть окно, если 0 - окно закрывается по нажатию юзером любой кнопки,
# либо можно выставить время ожидания в миллисекундах
cv2.destroyAllWindows()  # закрывает все окна
