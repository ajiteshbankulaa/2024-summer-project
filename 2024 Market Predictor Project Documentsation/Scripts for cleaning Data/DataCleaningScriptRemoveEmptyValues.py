import pandas as pd

# Load the CSV data
file_path1 = '/content/1111.22.csv'  # Change to your first file path
file_path2 = '/content/222.csv'  # Change to your second file path

df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)

# Ensure the date columns are in datetime format
df1['date'] = pd.to_datetime(df1['Date'])
df2['date'] = pd.to_datetime(df2['date'])

# Merge the dataframes on the 'date' column to keep only common dates
merged_df = pd.merge(df1, df2, on='date', how='inner')

# Save the merged dataframe to inspect the columns
merged_df.to_csv('merged_file.csv', index=False)

# Separate the merged dataframe back into two dataframes
df1_columns = df1.columns
df2_columns = df2.columns

df1_cleaned = merged_df[df1_columns]
df2_cleaned = merged_df[df2_columns]

# Save the cleaned data to new CSV files
cleaned_file_path1 = '/content/cl1.csv'
cleaned_file_path2 = '/content/cl2.csv'

df1_cleaned.to_csv(cleaned_file_path1, index=False)
df2_cleaned.to_csv(cleaned_file_path2, index=False)

print(f"Cleaned data saved to {cleaned_file_path1} and {cleaned_file_path2}")
