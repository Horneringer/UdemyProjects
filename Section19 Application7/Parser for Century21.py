import requests
import pandas
from bs4 import BeautifulSoup

r = requests.get('https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')

c = r.content

soup = BeautifulSoup(c, 'html.parser')

# получаем список со всеми div, у которых класс propertyRow
all = soup.find_all('div', {'class': 'propertyRow'})

# получаем доступ к номеру последней страницы
page_num = soup.find_all('a', {'class':'Page'})[-1].text

# создаём словарь, в качестве элементов будем хранить словари, каждый из которых имеет по 8 пар key:value
lst = []

# записываем базовый URL в переменную; у s нет значения
base_url = 'https://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='

# выведем адреса всех страниц по порядку вместе с их содержимым
# итерируемся по страницам от первой(индекс 0) до последней (извлеченный ранее page_num)
for page in range(0, int(page_num) * 10, 10):
    print(base_url + str(page) + '.html')
    r = requests.get(base_url + str(page) + '.html')
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')

    # с помощью цикла получаем список со всеми div, у которых класс propertyRow, для каждой страницы
    all = soup.find_all('div', {'class': 'propertyRow'})
    
    #  ---------------------------------цикл обработки данных для одной страницы------------------------------------------------------
    
    # цена; проходим по всем элементам списка all и извлекаем все тэги h4 c классом propPrice
    for item in all:
        dct = {}
        
        # для полученных значений цены задаём ключ Price
        dct['Price'] = item.find('h4', {'class': 'propPrice'}).text.replace('\n', '')
        
        # адрес; извлекаем адрес по тэгу span; каждая строка адреса содержится в отдельном классе,
        # чтобы извлеч оба, используем find_all
        
        # для первой части адреса задаём ключ Address
        dct['Address'] = item.find_all('span', {'class': 'propAddressCollapse'})[0].text
        
        # для второй - Locality
        dct['Locality'] = item.find_all('span', {'class': 'propAddressCollapse'})[1].text
        
        # beds; извлекаем количество спальных комнат; у первого элемента отсутствует информация о комнатах, отобразится
        # None, этот тип нельзя преобразовать в текст, используем исключение; чтобы извлечь только число, используем
        # метод find второй раз для поиска внутри класса span по тэгу b
        
        try:
            # задаём ключ Beds
            dct['Beds'] = item.find('span', {'class': 'infoBed'}).find('b').text
        except:
            # отсутствующая информация будет отображаться в таблице как None
            dct['Beds'] = None
        
        # baths; то же делаем с количеством ванных комнат
        try:
            # задаём ключ Baths
            dct['Baths'] = item.find('span', {'class': 'infoValueFullBath'}).find('b').text
        except:
            dct['Baths'] = None
        
        # area; с жилой площадью
        try:
            # задаём ключ Area
            dct['Area'] = item.find('span', {'class': 'infoSqFt'}).find('b').text
        except:
            dct['Area'] = None
        
        # half baths; с количеством полуваннх комнатами
        try:
            # задаём ключ Half baths
            dct['Half baths'] = item.find('span', {'class': 'infoValueHalfBath'}).find('b').text
        except:
            dct['Half baths'] = None
        
        # с помощью внутреннего цикла извлекаем особенности собственности(features);
        # находим все div с классом columnGroup
        
        for column_group in item.find_all('div', {'class': 'columnGroup'}):
            
            # Lot Size; с помощью функции zip проходим одновременно по двум спискам futureGroup и futureName и ставим их
            # значения попарно в соответствие; если в первом списке присутствует строка Lot Size, извлекаем
            # соответствующее этому значение из вторго списка
            
            for feature_group, feature_name in zip(column_group.find_all('span', {'class': 'featureGroup'}),
                                                   column_group.find_all('span', {'class': 'featureName'})):
                if 'Lot Size' in feature_group.text:
                    # задаём ключ Lot size
                    dct['Lot size'] = feature_name.text
        
        lst.append(dct)

# создаём датафрейм и передаём ему наш список словарей
df = pandas.DataFrame(lst)

# конвертируем датафрейм в csv файл
df.to_csv('Output.csv')


