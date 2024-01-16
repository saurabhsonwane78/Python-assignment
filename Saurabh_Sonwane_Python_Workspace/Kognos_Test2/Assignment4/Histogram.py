# Script for Histogram:

import pandas as pd
import matplotlib.pyplot as plt

data_path = 'E:\personal projects\Saurabh_Sonwane_Python_Workspace\Datasets\data.csv'
df = pd.read_csv(data_path)

# Extract data for histogram (assuming 'DT1' is the column name)
column_b_data = df['DT1']

# Plot histogram
plt.hist(column_b_data, bins=10, color='blue', edgecolor='black')
plt.xlabel('DT1')
plt.ylabel('Frequency')
plt.title('Histogram for DT1')
plt.show()


