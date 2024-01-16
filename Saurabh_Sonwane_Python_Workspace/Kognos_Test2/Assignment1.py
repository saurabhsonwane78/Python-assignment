import pandas as pd

excel_file_path = 'E:\personal projects\Saurabh_Sonwane_Python_Workspace\Datasets\ExcelTestData1.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Print values row by row
for index, row in df.iterrows():
    print(f"Row {index + 1}: {row.values}")

