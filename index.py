import pandas as pd

# Load your dataset
data = pd.read_csv('your_dataset.csv')

# Optionally, if you need to handle case sensitivity in titles or other string fields:
data['Title_normalized'] = data['Title'].str.lower()

# Step 1: Remove duplicates based on 'Title_normalized'
data = data.drop_duplicates(subset='Title_normalized', keep='first')

# Optionally, exclude rows where 'ISSN' and 'DOI' are NaN before further deduplication
data_non_nan = data.dropna(subset=['ISSN', 'DOI'])

# Remove duplicates based on 'ISSN' and 'DOI' where they exist and are not NaN
data_non_nan = data_non_nan.drop_duplicates(subset=['ISSN', 'DOI'], keep='first')

# Combine the data that was excluded in the NaN removal step with the deduplicated data
final_data = pd.concat([data_non_nan, data[data['ISSN'].isna() | data['DOI'].isna()]], ignore_index=True)

# Save the cleaned data to a new CSV file
final_data.to_csv('cleaned_dataset.csv', index=False)

print("Dataset cleaned and saved as 'cleaned_dataset.csv'.")
