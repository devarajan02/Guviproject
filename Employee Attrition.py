import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
df = pd.read_csv("employee_attrition.csv")  # Update with actual file path

# Display basic info and check for missing values
print(df.info())
print(df.isnull().sum())

# EDA - Visualizing Attrition
sns.countplot(x='Attrition', data=df)
plt.title("Employee Attrition Distribution")
plt.show()

# Correlation heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

# Convert categorical variables to numerical using Label Encoding
encoder = LabelEncoder()
categorical_features = df.select_dtypes(include=['object']).columns
for col in categorical_features:
    df[col] = encoder.fit_transform(df[col])

# Splitting data into features and target variable
X = df.drop(columns=['Attrition'])  # Features
y = df['Attrition']  # Target

# Standardize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
