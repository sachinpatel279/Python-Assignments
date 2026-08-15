import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "-" * 50

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

X = df.drop("FinalResult", axis=1)
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

Depths = [1, 3, None]

print(Border)
print("Testing Accuracy for Different Tree Depths")
print(Border)

for depth in Depths:

    model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    Accuracy = accuracy_score(y_test, y_pred)

    print("Max Depth =", depth)
    print("Testing Accuracy =", Accuracy * 100, "%")
    print(Border)