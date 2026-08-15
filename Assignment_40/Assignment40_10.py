import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "-" * 50

print(Border)
print("Decision Tree with max_depth = None")
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
    max_depth=None,
    random_state=42
)


model.fit(X_train, Y_train)

train_pred = model.predict(X_train)

test_pred = model.predict(X_test)

train_accuracy = accuracy_score(
    Y_train,
    train_pred
)

test_accuracy = accuracy_score(
    Y_test,
    test_pred
)

print("\nTraining Accuracy :", round(train_accuracy * 100, 2), "%")

print("Testing Accuracy  :", round(test_accuracy * 100, 2), "%")

if train_accuracy == 1.0 and test_accuracy < 1.0:

    print("\nObservation:")
    print("Training accuracy is 100% but testing accuracy is lower.")
    print("This is called Overfitting.")
    print("The model has memorized the training data")
    print("and does not generalize well to new data.")

else:

    print("\nThe model is not showing significant overfitting.")