# Script for Box Plot

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_path = 'E:\personal projects\Saurabh_Sonwane_Python_Workspace\Datasets\data.csv'
df = pd.read_csv(data_path)

# Extract data for box plot (assuming 'Rhob1' is the column name)
column_c_data = df['Rhob1']

# Plot box plot using seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.boxplot(x=column_c_data, color='green')
plt.xlabel('Rhob1')
plt.title('Box Plot for Rhob1')
plt.show()