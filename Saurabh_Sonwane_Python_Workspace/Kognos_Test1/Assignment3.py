import pandas as pd

file_path = 'E:\personal projects\Saurabh_Sonwane_Python_Workspace\Datasets\Mud_Weight.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Multiply the 'Mud_Weight' column by 10
df['Mud_Weight'] = df['Mud_Weight'] * 10

# Display the modified DataFrame
print(df)

# Save the modified DataFrame to a new CSV file
output_file_path = 'path/to/Mud_Weight_Modified.csv'
df.to_csv(output_file_path, index=False)

print(f"Multiplication completed. Data saved to {output_file_path}")
