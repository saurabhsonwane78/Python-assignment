import pandas as pd

file_path = 'E:\personal projects\Saurabh_Sonwane_Python_Workspace\Datasets\Mud_Weight.csv'
df = pd.read_csv(file_path)
conversion_factor = 119.826

# Convert the second column data
df['Mud_Weight'] = df['Mud_Weight'] * conversion_factor

# Save the modified DataFrame to a new CSV file
output_file_path = '/'
df.to_csv(output_file_path, index=False)
print(f"Conversion completed. Data saved to {output_file_path}")
