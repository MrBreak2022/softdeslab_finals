import os
import pandas as pd

# Load the dataset
diabetes_filepath = 'A:/School Files/4th Year files/softdes/softdeslab_finals_v2/Diabetes.csv'
diabetes_df = pd.read_csv(diabetes_filepath)

# Step 1: Display dataset structure information
diabetes_df.info()
print(diabetes_df.head())

print("Unique values in 'Gender' column before mapping:", diabetes_df['Gender'].unique())

#  Male = 0 & Female = 1 
gender_mapping = {'Male': 0, 'Female': 1, 'M': 0, 'F': 1}
diabetes_df['Gender'] = diabetes_df['Gender'].map(gender_mapping)

# Check unique values in the 'Gender' column after mapping
print("Unique values in 'Gender' column after mapping:", diabetes_df['Gender'].unique())

# Convert 'Gender' to numeric to coerce any remaining non-numeric values to NaN
diabetes_df['Gender'] = pd.to_numeric(diabetes_df['Gender'], errors='coerce')

# Fill missing values in 'Gender' with the mode
if diabetes_df['Gender'].isna().sum() > 0:
    diabetes_df['Gender'].fillna(diabetes_df['Gender'].mode()[0], inplace=True)

# Ensure 'Gender' column is of integer type
diabetes_df['Gender'] = diabetes_df['Gender'].astype(int)

# Map CLASS values ('N' -> 0, 'Y' -> 1, 'P' -> 2)
# Class: Negative (N), Positive (Y), P (Possible)
class_mapping = {'N': 0, 'Y': 1, 'P': 2}
diabetes_df['CLASS'] = diabetes_df['CLASS'].map(class_mapping)

# Drop rows with NaN values in any columns left, especially after mapping
data = diabetes_df.dropna()

# Display final dataset info to verify changes
print(data.info())

# Save the preprocessed data
directory = 'datasets'
if not os.path.exists(directory):
    os.makedirs(directory)

filepath = os.path.join(directory, 'preprocessed_diabetes.csv')
data.to_csv(filepath, index=False)

# Confirm file save
if os.path.exists(filepath):
    print('File saved successfully')
else:
    print('File did not save')