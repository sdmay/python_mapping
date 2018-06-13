import folium
import pandas

# import the data using pandas to read the file
data = pandas.read_csv('Volcanoes_USA.txt')

# set the data to a list and assign the attributes to variables
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
mtnames = list(data['NAME'])
# function to return a color value based on mountain range elevation(elev)
def color_range(e):
        # print(e)
        if e < 1500:
            return 'green'
        elif e < 1500 and e < 2500:
            return 'blue'
        elif e > 2500 and e < 5000:
            return 'orange'
        else:
            return 'aquamarine'
# generate the origin point of your map, zoom level, and map type
map = folium.Map(location=[36, -102], zoom_start=4, tiles='Mapbox Bright')

#Set feature groups for scalable cleaner code
fgv = folium.FeatureGroup(name='Volcanoes')
fgp = folium.FeatureGroup(name='Population')
def get_names(x):
    # y = str(x)
    # return folium.Popup(x)
    return folium.Popup(x, parse_html=True)


# Using the zip fuction keeps the index value of the lists and can place them in the proper location in the function
for lt, ln, el, n in zip(lat, lon, elev, mtnames):
    # Create a popup that takes in a string and is able to be parsed in HTML
        # popup = folium.Popup(html=n, parse_html=True)

    # create circle markers for the volcanoes based on lat and lon, color is the border
        fgv.add_child(folium.CircleMarker(location=[lt, ln],  radius=5, popup=get_names(n),  fill_color=color_range(el), color=color_range(el), fill_opacity=0.7, fill=True ))
    # append the volcano circle markers to the map

# open the json file to retreive the population data.  Set polygons from GeoJson to a specific color based on the number of people
fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()), style_function= lambda x: {'fillColor': 'red ' if x['properties']['POP2005'] <15000000
else 'orange' if 15000000 <= x['properties']['POP2005'] < 25000000 else 'green' if 25000000 <= x['properties']['POP2005'] < 50000000 else 'blue' if 50000000 <= x['properties']['POP2005'] < 60000000000000 else 'purple'}))
# append population to the map
map.add_child(fgp)
map.add_child(fgv)
# turn on layer control to toggle layers
map.add_child(folium.LayerControl())
# save map to file to open in browser
map.save('Map1.html')
