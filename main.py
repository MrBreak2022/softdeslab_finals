import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load the preprocessed dataset
file_path = 'datasets/preprocessed_diabetes.csv'
data = pd.read_csv(file_path)


