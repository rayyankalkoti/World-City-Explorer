import folium

# Sample data - replace with accurate data from reliable sources
city_data = [
    {'name': 'Bangkok', 'lat': 13.7563, 'lon': 100.5018, 'rank': 1, 'visitors': 22.78},
    {'name': 'Paris', 'lat': 48.8566, 'lon': 2.3522, 'rank': 2, 'visitors': 19.10},
    {'name': 'London', 'lat': 51.5074, 'lon': -0.1278, 'rank': 3, 'visitors': 19.09},
    {'name': 'Dubai', 'lat': 25.2048, 'lon': 55.2708, 'rank': 4, 'visitors': 15.93},
    {'name': 'Singapore', 'lat': 1.3521, 'lon': 103.8198, 'rank': 5, 'visitors': 14.67},
    {'name': 'Kuala Lumpur', 'lat': 3.1390, 'lon': 101.6869, 'rank': 6, 'visitors': 13.79},
    {'name': 'New York City', 'lat': 40.7128, 'lon': -74.0060, 'rank': 7, 'visitors': 13.60},
    {'name': 'Istanbul', 'lat': 41.0082, 'lon': 28.9784, 'rank': 8, 'visitors': 13.40},
    {'name': 'Tokyo', 'lat': 35.6762, 'lon': 139.6503, 'rank': 9, 'visitors': 12.93},
    {'name': 'Antalya', 'lat': 36.8869, 'lon': 30.7026, 'rank': 10, 'visitors': 12.41},
    # Add more cities up to 20 with accurate data
]

# Create base map
m = folium.Map(location=[20, 0], zoom_start=2, tiles='OpenStreetMap')

# Add markers for each city
for city in city_data:
    popup_text = f"""
    <b>{city['name']}</b><br>
    Rank: {city['rank']}<br>
    Visitors: {city['visitors']} million
    """
    folium.CircleMarker(
        location=[city['lat'], city['lon']],
        radius=5,
        color='blue',
        fill=True,
        fill_color='blue',
        popup=folium.Popup(popup_text, max_width=250),
        tooltip=f"{city['name']} (#{city['rank']})"
    ).add_to(m)

# Save to HTML file
m.save('most_visited_cities.html')
print("Map saved to most_visited_cities.html")