import pandas as pd

# Load the CSV data
file_path = '/content/adad.csv'  # Change to your file path
df = pd.read_csv(file_path, header=None, names=['Date', 'Value'])

# Filter out rows where the 'Value' column is '.'
df_cleaned = df[df['Value'] != '.']

# Save the cleaned data to a new CSV file
cleaned_file_path = '/content/ototaota'
df_cleaned.to_csv(cleaned_file_path, index=False, header=False)

print(f"Rows with '.' in the second column have been removed. Cleaned data saved to {cleaned_file_path}")