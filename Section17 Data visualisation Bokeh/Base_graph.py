from bokeh.io import output_file, show
from bokeh.plotting import figure
import pandas

# считываем файл по ссылке и парсим столбец Data
df = pandas.read_csv('adbe.csv', parse_dates=['Date'])

# задаём ширину и высоту графика, указываем тип данных для оси X
p = figure(width=500, height=250, x_axis_type='datetime')

# передаём объекту нужные колонки, цвет линии и прозрачность
p.line(df['Date'], df['Close'], color='Blue', alpha=0.5)

output_file('Timeseries.html')

show(p)
