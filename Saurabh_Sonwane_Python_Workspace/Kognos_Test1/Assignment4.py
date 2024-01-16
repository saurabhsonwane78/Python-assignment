import pandas as pd
import h5py

# Replace 'path/to/your/Survey_Data.csv' with the actual path to your CSV file
csv_file_path = 'E:\personal projects\Saurabh_Sonwane_Python_Workspace\Datasets\Survey_Data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Create an HDF5 file and store data in the 'DATA' dataset
hdf_file_path = 'Survey.h5'
with h5py.File(hdf_file_path, 'w') as hdf:
    # Create a float dataset named 'DATA' and store DataFrame values
    hdf.create_dataset('DATA', data=df.values, dtype='float64')

print(f"Data written to {hdf_file_path}")
