# модуль для считывания данных с онлайн ресурсов/различных компаний
from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file

# модуль компонентов из интерфейса встраивания Bokeh
from bokeh.embed import components

start_data = datetime.datetime(2018, 9, 1)
end_data = datetime.datetime(2018, 9, 24)

# в параметры передаём имя компании(в данном случае запасное имя Google), источник данных,
# промежуток времени, из которого получаем данные; тип dataframe
df = data.DataReader(name='GOOG', data_source='yahoo', start=start_data, end=end_data)


# создаём новый столбец в датафрейме, обозначающий статус цены(увеличивается или уменьшается)
# значение в каждой ячейке будет устанавливаться в зависимости от цен на открытие или закрытие в этот день

def inc_dec(cl, op):
    if cl > op:
        value = 'Increase'
    elif cl < op:
        value = 'Decrease'
    else:
        value = 'Equal'
    return value


# устанавливаем статус с помощью функции, перебирая в цикле все дни со значениями close open попарно
df['Status'] = [inc_dec(cl, op) for cl, op in zip(df.Close, df.Open)]

# создаём столбец с координатами середины прямоугольника по Y
df['Middle'] = (df.Close + df.Open) / 2

# столбец для высоты
df['Height'] = abs(df.Close - df.Open)

p = figure(x_axis_type='datetime', width=1500, height=800)

# график масштабируется вместе с окном(вместо устаревшего responsive = True)
p.sizing_mode = "scale_both"

# заголовок диаграммы
p.title.text = ('Candlestick Chart')

# устанавливаем прозрачность сетки(от 0 до 1)
p.grid.grid_line_alpha = 0.3

# переводим 12 часов в миллисекунды
hours_12 = 12 * 60 * 60 * 1000

# используем сегменты для отображения максимальной и минимальной цены за день;
# 4 параметра: x,y координаты верхней точки и x,y координаты нижней точки
# отрисовываем сегменты до прямоугольников, так как в Bokeh новые слои накладываются поверх старых

p.segment(df.index, df.High, df.index, df.Low, color='black')

# определем координаты центров прямоугольника; координаты по оси X - даты, когда в столбце Status значение Increase
# (цена закрытия торгов выше цены открытия)
# строки индексируются по дате, поэтому используем index
# координаты по оси Y - сумма цен открытия и закрытия попалам, вычисляется в столбце Middle;
# ширина прямоугольников будет 12 часов(откладывается + и - 6 часов от центра)
# высота - разница между ценой закрытия и открытия, столбец Height
# указываем цвет прямоугольников и цвет границ в формате CSS

p.rect(df.index[df.Status == 'Increase'], df.Middle[df.Status == 'Increase'],
       hours_12, df.Height[df.Status == 'Increase'], fill_color='#CCFFFF', line_color='black')

# координаты по оси X - даты, когда в столбце Status значение Decrease
# (цена закрытия торгов ниже цены открытия), цвет прямоугольников красный

p.rect(df.index[df.Status == 'Decrease'], df.Middle[df.Status == 'Decrease'],
       hours_12, df.Height[df.Status == 'Decrease'], fill_color='#FF3333', line_color='black')

# отображение графика в локальном html файле, сохраняется на компе
# output_file('CS.html')

# show(p)
