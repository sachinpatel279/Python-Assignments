import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

Border = "-" * 50

print(Border)
print("Confusion Matrix and Classification Report")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

X = df.drop(columns=["FinalResult"])

Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(
    random_state=42
)

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

cm = confusion_matrix(
    Y_test,
    Y_pred
)

print("\nConfusion Matrix")
print(cm)

print("\nClassification Report")

print(
    classification_report(
        Y_test,
        Y_pred
    )
)