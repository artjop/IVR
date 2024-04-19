import folium
import requests


# Координаты области, которую мы хотим показать на карте
north = 55.7661
south = 55.7540
east = 37.6490
west = 37.6279

# Создаем объект карты с центром в середине этой области
m = folium.Map(location=[(north + south) / 2, (east + west) / 2], zoom_start=15)

# Отправляем запрос к серверу OSM для получения объектов в этой области
response = requests.get(f'https://www.openstreetmap.org/api/0.6/map?bbox={west},{south},{east},{north}')

# Преобразуем ответ сервера в XML-документ и извлекаем все объекты с тегом "amenity=restaurant"
xml = response.text
red_objects = []
for element in xml.split('</node>'):
    if 'amenity="restaurant"' in element:
        lat = float(element.split('lat="')[1].split('"')[0])
        lon = float(element.split('lon="')[1].split('"')[0])
        folium.Marker([lat, lon], icon=folium.Icon(color='red')).add_to(m)

# Сохраняем карту в файл
m.save('map.html')
