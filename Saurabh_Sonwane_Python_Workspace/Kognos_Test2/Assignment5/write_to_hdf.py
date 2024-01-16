import pandas as pd
import h5py

# Read data from Excel (replace 'path/to/your/excel_file.xlsx' with the actual path)
excel_file_path = 'E:\personal projects\Saurabh_Sonwane_Python_Workspace\Datasets\excel_file.xlsx'
df = pd.read_excel(excel_file_path)

# Create an HDF file and write data to a float dataset
hdf_file_path = 'test1.hdf'
with h5py.File(hdf_file_path, 'w') as hdf:
    float_dataset = hdf.create_dataset('float_data', data=df.values, dtype='float64')

print(f"Data written to {hdf_file_path}")
