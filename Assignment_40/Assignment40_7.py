import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "-" * 50

print(Border)
print("Compare Different random_state Values")
print(Border)


df = pd.read_csv("student_performance_ml.csv")

X = df.drop(columns=["FinalResult"])

Y = df["FinalResult"]


states = [0, 10, 42]

for state in states:

    print("\nRandom State :", state)
    print("-" * 30)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=state
    )

    model = DecisionTreeClassifier(
        random_state=state
    )

    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(
        Y_test,
        Y_pred
    )

    print(
        "Testing Accuracy :",
        round(accuracy * 100, 2),
        "%"
    )

print("\nObservation:")
print("Different random_state values may produce different train-test splits.")
print("Therefore, testing accuracy may change.")