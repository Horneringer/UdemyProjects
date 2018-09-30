# импортируем датафрэйм из нашего модуля motion_detector

from motion_detector import df
from bokeh.plotting import figure, output_file, show

# импортируем модуль инструмента зависания курсора и модуль столбчатых источников данных
from bokeh.models import HoverTool, ColumnDataSource

# конвертируем дату начала и конца в строку и задаём формат отображения
df['Start_string'] = df['Start'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['End_string'] = df['End'].dt.strftime('%Y-%m-%d %H:%M:%S')

# создаём объект класса ColumnarDataSource и предаём ему датафрэйм
col_data_src = ColumnDataSource(df)

# создаём объект, указываем размеры и заголовок графика
p = figure(x_axis_type='datetime', width=800, height=400, title='Motion graph')

# убираем деления оси Y, устанавливая их (цвет в None
p.yaxis.minor_tick_line_color = None

# устанавливаем количество делений сетки
p.ygrid[0].ticker.desired_num_ticks = 1

# создаём объект класса HoverTool; tooltips - всплывающие подсказки, представляет собой список картежей,
# в которые через декоратор из csv файла передаётся содержимое столбцов (информация начала и конца события);
#  отображается во всплывающем окне
hover = HoverTool(tooltips=[('Start ', '@Start_string'), ('End ', '@End_string')])

# добавляем инструмент на график с помощью метода add_tools
p.add_tools(hover)

# задаём тип глифа для графика - квадрант,
#  указываем источник данных(позволяет не использовать конструкцию left = df['Start'])
q = p.quad(top=1, bottom=0, left='Start', right='End', color='green', source=col_data_src)

output_file('Graph.html')

show(p)
