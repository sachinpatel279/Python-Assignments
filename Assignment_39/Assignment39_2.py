####################################################
# Decision Tree Classification
####################################################

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

Border = "-" * 50

####################################################
# Step 1: Load the dataset
####################################################

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

####################################################
# Step 2: Separate features and label
####################################################

X = df.drop("FinalResult", axis=1)

y = df["FinalResult"]

####################################################
# Step 3: Split dataset
####################################################

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

####################################################
# Create and train Decision Tree model
####################################################

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

print(Border)
print("Model trained successfully")
print(Border)

####################################################
# Predict X_test values
####################################################

y_pred = model.predict(X_test)

Result = pd.DataFrame({
    "Actual Value": y_test.values,
    "Predicted Value": y_pred
})

print("Actual and Predicted Values")
print(Border)

print(Result)
