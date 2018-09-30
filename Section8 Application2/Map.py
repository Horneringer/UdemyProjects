import folium
import pandas

df = pandas.read_csv("Volcanoes_USA.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])
nm = list(df["NAME"])


def colour_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="MapBox Bright")

fg_v = folium.FeatureGroup(name="Вулканы")

for lt, ln, el in zip(lat, lon, elev):
    fg_v.add_child(
        folium.CircleMarker(location=[lt, ln], popup=str(el) + ' м', fill=True, fill_color=colour_producer(el),
                            color='grey', fill_opacity=1, radius=8))

fg_p = folium.FeatureGroup(name="Население")

fg_p.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                              style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fg_v)
map.add_child(fg_p)
map.add_child(folium.LayerControl())
map.save("Map1.html")
