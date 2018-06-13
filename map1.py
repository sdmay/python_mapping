import folium
import pandas

data = pandas.read_csv('Volcanoes_USA.txt')
# print(data)
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

def color_range(e):

        print(e)
        if e < 1500:
            return 'green'
        elif e < 1500 and e < 2500:
            return 'blue'
        elif e > 2500 and e < 5000:
            return 'orange'
        else:
            return 'aquamarine'

map = folium.Map(location=[36, -102], zoom_start=4, tiles='Stamen Terrain')

fgp = folium.FeatureGroup(name='Volcanoes')
fgv = folium.FeatureGroup(name='Population')

for lt, ln, el, n in zip(lat, lon, elev, name):
    popup = folium.Popup(n ,parse_html=True)
    fgp.add_child(folium.CircleMarker(location=[lt, ln], popup=popup, radius=5, fill_color=color_range(el), color=color_range(el), fill_opacity=0.7, fill=True ))
map.add_child(fgp)
fgv.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()), style_function= lambda x: {'fillColor': 'red ' if x['properties']['POP2005'] <15000000
else 'orange' if 15000000 <= x['properties']['POP2005'] < 25000000 else 'green' if 25000000 <= x['properties']['POP2005'] < 50000000 else 'blue' if 50000000 <= x['properties']['POP2005'] < 60000000000000 else 'purple'}))

# map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())


map.save('Map1.html')
