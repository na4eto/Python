import geocoder
import folium

g = geocoder.ip('185.117.83.255')

coords = g.latlng

map = folium.Map(location=coords,
                 zoom_start=12)

folium.CircleMarker(location=coords, radius=50, popup='Yorkshire').add_to(map)

folium.Marker(coords, popup='Person').add_to(map)

map.save("map.html ")
