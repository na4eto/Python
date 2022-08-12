import folium
import phonenumbers
from phonenumbers import carrier, geocoder
from opencage.geocoder import OpenCageGeocode

number = '+359886500512'

Key = 'e05fa2dce32b4b7eb33ff17d06e0d014'

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, 'en')
print(yourLocation)


# get the provider

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)


folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

# save map

myMap.save('phone_location_map.html')
