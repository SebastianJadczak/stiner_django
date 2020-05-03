import folium

# Create map

m = folium.Map(location=[52.2297700, 21.0117800], zoom_start=12)
# Global tooltip
tooltip = 'Kliknij po więcej informacji'

# Create markers
folium.Marker([52.2460643, 21.0140727] ,
              popup='<strong> Kościół św. Anny w Warszawie – świątynia rzymskokatolicka znajdująca się przy Krakowskim Przedmieściu 68 w dzielnicy Śródmieście, główny ośrodek duszpasterstwa akademickiego w Warszawie. Wikipedia</strong> ',
              tooltip=tooltip).add_to(m)


# Generate map
m.save('templates/map/map.html')
