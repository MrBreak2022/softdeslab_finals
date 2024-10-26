import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


# Load the dataset
diabetes_filepath = 'A:/School Files/4th Year files/softdes/softdeslab_finals_v2/Diabetes.csv'
diabetes_df = pd.read_csv(diabetes_filepath)

# Step 1: Display dataset structure information
diabetes_df.info()
diabetes_df.head()

