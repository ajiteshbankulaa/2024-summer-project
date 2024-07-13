import pandas as pd

# Read the CSV files
df1 = pd.read_csv('/content/USREC_Daily_Dates Put into colab.csv', sep=',')
df2 = pd.read_csv('/content/Dates.csv', sep=',')

# Print column names and first few rows to check for correctness
print("First file columns:", df1.columns)
print("Second file columns:", df2.columns)
print("First few rows of the first file:\n", df1.head())
print("First few rows of the second file:\n", df2.head())

# Rename the columns to ensure consistency
# Assuming the first file has columns like 'DATE' and 'VALUE'
df1.rename(columns={df1.columns[0]: 'DATE', df1.columns[1]: 'VALUE'}, inplace=True)
df2.rename(columns={df2.columns[0]: 'DATE'}, inplace=True)

# Convert 'DATE' columns to datetime format
df1['DATE'] = pd.to_datetime(df1['DATE'], errors='coerce')
df2['DATE'] = pd.to_datetime(df2['DATE'], errors='coerce')

# Drop rows with invalid dates (if any)
df1 = df1.dropna(subset=['DATE'])
df2 = df2.dropna(subset=['DATE'])

# Filter df1 to keep only the dates present in df2
filtered_df = df1[df1['DATE'].isin(df2['DATE'])]

# Check the filtered DataFrame
print("Filtered DataFrame:\n", filtered_df)

# Save the filtered DataFrame to a new file
output_file_path = '/content/filtered_file1.csv'  # Change to your desired output file path
filtered_df.to_csv(output_file_path, index=False, sep=',', header=True)

print(f"Filtered data saved to {output_file_path}")