import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the Taiwan county-level shapefile or GeoJSON
# 假設 county_mol 資料夾中有一個 GeoJSON 檔案，包含台灣各縣市的地理資料
taiwan_map = gpd.read_file('county_mol/COUNTY_MOI_1140318.shp.xml')

# Filter for 北北基及桃園 (台北市、新北市、基隆市、桃園市)
target_counties = ['台北市', '新北市', '基隆市', '桃園市']
filtered_map = taiwan_map[taiwan_map['COUNTYNAME'].isin(target_counties)]

# Load the bus route data
bus_data = pd.read_csv('20250520/bus_route_10417_tteback.csv', header=None, names=['StopID', 'StopName', 'Status'])

# Clean the data: Remove HTML tags from the 'Status' column
bus_data['Status'] = bus_data['Status'].str.replace(r'<.*?>', '', regex=True)

# Generate dummy coordinates for bus stops (for demonstration purposes)
# In a real scenario, you would replace this with actual latitude and longitude data
bus_data['Longitude'] = [121.5 + i * 0.01 for i in range(len(bus_data))]
bus_data['Latitude'] = [25.0 + i * 0.005 for i in range(len(bus_data))]

# Convert bus data to GeoDataFrame
bus_stops = gpd.GeoDataFrame(bus_data, geometry=gpd.points_from_xy(bus_data['Longitude'], bus_data['Latitude']))

# Plot the map
fig, ax = plt.subplots(figsize=(10, 10))
filtered_map.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=0.5)
bus_stops.plot(ax=ax, color='red', markersize=50, label='Bus Stops')

# Add labels for bus stops
for x, y, label in zip(bus_stops.geometry.x, bus_stops.geometry.y, bus_stops['StopName']):
    ax.text(x, y, label, fontsize=8, ha='right')

# Add title and legend
plt.title('北北基及桃園地圖與公車站牌路線', fontsize=16)
plt.legend()
plt.tight_layout()

# Save the map as an image
plt.savefig('20250520/north_taiwan_map_with_bus_stops.png')
plt.show()