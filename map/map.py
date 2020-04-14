import folium

# Create map

m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

# Generate map
m.save('templates/map/map.html')