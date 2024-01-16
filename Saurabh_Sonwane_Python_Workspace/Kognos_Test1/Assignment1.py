import pandas as pd
from matplotlib import pyplot as plt

file_path = 'E:\personal projects\Saurabh_Sonwane_Python_Workspace\Datasets\Mud_Weight.csv'
df = pd.read_csv(file_path)
plt.plot(df.Mud_Weight,df.MD)
plt.xlabel('Mud Weight Data')
plt.ylabel('Depth')
plt.show()