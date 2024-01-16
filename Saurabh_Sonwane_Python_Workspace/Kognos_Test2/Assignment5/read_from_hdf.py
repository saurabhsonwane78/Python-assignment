import h5py
import time

# Read data from the HDF file
hdf_file_path = 'test1.hdf'
with h5py.File(hdf_file_path, 'r') as hdf:
    float_dataset = hdf['float_data']
    num_columns = float_dataset.shape[1]

    # Calculate time taken to read and write text files
    start_time = time.time()

    # Extract data and write each column to a separate text file
    for i in range(num_columns):
        column_data = float_dataset[:, i]
        text_file_path = f'column_{i+1}.txt'
        with open(text_file_path, 'w') as text_file:
            for value in column_data:
                text_file.write(f"{value}\n")

    end_time = time.time()
    elapsed_time = end_time - start_time

print(f"Text files written. Time taken: {elapsed_time:.2f} seconds")
