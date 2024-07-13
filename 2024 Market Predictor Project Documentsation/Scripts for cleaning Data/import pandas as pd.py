import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('contentsample_dataDates.csv', sep=',')

print(df.columns)

# Convert 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d')

# Set 'DATE' column as the index
df.set_index('DATE', inplace=True)

# Resample to daily frequency and forward fill missing values
df_daily = df.resample('D').ffill()

# Reset index and format the output
df_daily.reset_index(inplace=True)
df_daily['DATE'] = df_daily['DATE'].dt.strftime('%m%d%Y')

# Save the output to a new CSV file
df_daily.to_csv('contentoutput.csv', index=False)

print(Output CSV file generated successfully.)