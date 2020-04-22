import folium

# Create map

m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)
# Global tooltip
tooltip = 'Kliknij po więcej informacji'

# Create markers
folium.Marker([42.3601, -71.0589] ,
              popup='<strong> Pierwszy punkt na mapie </strong> <a href="/management/blog_/">Więcej</a>',
              tooltip=tooltip).add_to(m)

folium.Marker([42.36201, -71.1589],
              popup='<strong> Pierwszy punkt na mapie </strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to(m)

# Generate map
m.save('templates/map/map.html')
