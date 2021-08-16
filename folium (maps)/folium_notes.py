import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elevation = list(data["ELEV"])

#-------------------------------
html = """      
<h4>Volcano information:<h4>
Height: %s m
"""     # #html stuff, ???
#-------------------------------

map = folium.Map(location=[38.85, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")


fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 80000000 else 'red'}))


def color_picker(elevation):
    if elevation < 2000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'


for lt, ln, el in zip(lat, lon, elevation):
    #-----------------------------------------------------------------------------------
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)  #html stuff, ???
    #-----------------------------------------------------------------------------------
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe),
    fill_color=color_picker(el), color='grey', fill = True, fill_opacity=.7))    #adding features to "My Map" feature group


map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl(position='bottomright')) # have to put after feature group, LayerControl will look for layers that aren't there yet
# My Map is the FeatureGroup name

map.save("Map1.html")
