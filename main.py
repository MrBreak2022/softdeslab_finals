import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
diabetes_filepath = 'A:/School Files/4th Year files/softdes/softdeslab_finals_v2/Diabetes.csv'
diabetes_df = pd.read_csv(diabetes_filepath)

# Step 1: Display dataset structure information
diabetes_df.info()
diabetes_df.head()

# Step 2: Summary Statistics
diabetes_df.describe()

# Step 3: Missing Values Summary
diabetes_df.isna().sum()

# Step 4: Class Distribution
class_distribution = diabetes_df['CLASS'].value_counts(normalize=True) * 100

# class distribution
print(class_distribution)

# Plot


# Plotting distributions for each numerical feature
numerical_columns = diabetes_df.select_dtypes(include=['int64', 'float64']).columns.drop(['ID', 'No_Pation'])

# Plotting histograms for numerical columns
for column in numerical_columns:
    plt.figure(figsize=(8, 4))
    plt.hist(diabetes_df[column], bins=30, edgecolor='black', alpha=0.7)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

import seaborn as sns

# Boxplots for each numerical feature to visualize potential outliers
plt.figure(figsize=(15, 8))
sns.boxplot(data=diabetes_df[numerical_columns], orient="h")
plt.title("Boxplot of Numerical Features")
plt.xlabel("Value Range")
plt.show()

# Heatmap to show correlations between numerical features
plt.figure(figsize=(12, 8))
correlation_matrix = diabetes_df[numerical_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Heatmap of Feature Correlations")
plt.show()
