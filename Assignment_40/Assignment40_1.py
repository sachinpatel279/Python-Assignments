import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = "-" * 50

print(Border)
print("Feature Importance")
print(Border)

# Load dataset
df = pd.read_csv("student_performance_ml.csv")

# Separate features and label
X = df.drop(columns=["FinalResult"])
Y = df["FinalResult"]

# Split dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

# Create model
model = DecisionTreeClassifier(random_state=42)

# Train model
model.fit(X_train, Y_train)

importance = model.feature_importances_

print("\nImportance of Each Feature")

for feature, value in zip(X.columns, importance):
    print(feature, ":", round(value, 4))

max_index = importance.argmax()

min_index = importance.argmin()

print("\nMost Important Feature :", X.columns[max_index])

print("Least Important Feature :", X.columns[min_index])