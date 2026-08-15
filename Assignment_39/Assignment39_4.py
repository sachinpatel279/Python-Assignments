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

####################################################
# Calculate testing accuracy
####################################################

TestingAccuracy = accuracy_score(y_test, y_pred)

print(Border)
print("Testing Accuracy")
print(Border)

print("Accuracy :", TestingAccuracy * 100, "%")

####################################################
# Generate Confusion Matrix
####################################################

cm = confusion_matrix(y_test, y_pred)

print(Border)
print("Confusion Matrix")
print(Border)

print(cm)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
)

display.plot()

plt.title("Decision Tree Confusion Matrix")

plt.show()

####################################################
# Extract TN, FP, FN and TP
####################################################

TN, FP, FN, TP = cm.ravel()

print(Border)
print("Confusion Matrix Values")
print(Border)

print("True Negative  :", TN)
print("False Positive :", FP)
print("False Negative :", FN)
print("True Positive  :", TP)
