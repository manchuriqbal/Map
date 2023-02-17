import folium
import pandas

data = pandas.read_csv(open("Volcanoes_USA.txt", "r"))
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def marker_color(elevation):
    if elevation < 2000:
        return "green"
    elif elevation < 3000:
        return "yellow"
    else:
        return "red"


map = folium.Map(location=[38.02, -99.09],
                 zoom_start=6, TileLayer="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for la, lo, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(
        location=[la, lo], radius=6, popup=str(el) + " m", fill=True, fillColor=marker_color(el), fill_opacity=0.70, color="gray"))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(
    data=open("world.json", "r", encoding='utf-8-sig').read(),
    style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 1000000
                              else "yellow" if x["properties"]["POP2005"] < 10000000
                              else "blue" if x["properties"]["POP2005"] < 100000000 else "red"}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map3.html")
