import json
import urllib.request
import folium
import pandas as pd
import auxiliaryFunctions
from folium.plugins import HeatMap

file_path = '/Users/khushanshahad/Desktop/hauntings.csv'
dataframe = pd.read_csv(file_path)

dataframe['latitude'] = pd.to_numeric(dataframe['latitude'], errors='coerce')
dataframe['longitude'] = pd.to_numeric(dataframe['longitude'], errors='coerce')

# Keep only Chicago hauntings (in Illinois, to avoid other cities named Chicago)
chicago_df = dataframe[
    (dataframe['state'].str.strip().str.lower() == 'illinois') &
    (dataframe['city'].str.strip().str.lower() == 'chicago')
].copy()
chicago_df = chicago_df.dropna(subset=['latitude', 'longitude'])

# Base map centered on Chicago
chicago_map = folium.Map(location=[41.8781, -87.6298], zoom_start=11)

# Download the Chicago city boundary
boundary_url = "https://data.cityofchicago.org/api/geospatial/qqq8-j68g?method=export&format=GeoJSON"
with urllib.request.urlopen(boundary_url) as response:
    chicago_geojson = json.load(response)

# Draw the outline (no fill so the heatmap stays visible)
folium.GeoJson(
    chicago_geojson,
    name="Chicago Outline",
    style_function=lambda feature: {
        "fillColor": "orange",
        "color": "black",
        "weight": 1.5,
    },
).add_to(chicago_map)

# Heatmap
heat_data = chicago_df[['latitude', 'longitude']].values.tolist()
HeatMap(heat_data).add_to(chicago_map)

chicago_map.save('index.html')

auxiliaryFunctions.stats(chicago_df)
auxiliaryFunctions.success_message()