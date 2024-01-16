import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

csv_file_path = 'E:\personal projects\Saurabh_Sonwane_Python_Workspace\Datasets\Latitude_Long_Example_Data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Create a GeoDataFrame from the DataFrame by specifying the geometry
geometry = gpd.points_from_xy(df['Longitude'], df['Latitude'])
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Plot the GIS data
gdf.plot(marker='o', color='blue', markersize=5, alpha=0.5)
plt.title('GIS Data Plot')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
