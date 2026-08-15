import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "-" * 50

print(Border)
print("PerformanceIndex Feature")
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

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

accuracy1 = accuracy_score(Y_test, Y_pred)

df["PerformanceIndex"] = (
    df["StudyHours"] * 2
) + df["Attendance"]

X2 = df.drop(columns=["FinalResult"])

Y2 = df["FinalResult"]

X_train2, X_test2, Y_train2, Y_test2 = train_test_split(
    X2,
    Y2,
    test_size=0.2,
    random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)

model2.fit(X_train2, Y_train2)

Y_pred2 = model2.predict(X_test2)

accuracy2 = accuracy_score(Y_test2, Y_pred2)

print("\nOriginal Accuracy :", round(accuracy1 * 100, 2), "%")

print("New Accuracy      :", round(accuracy2 * 100, 2), "%")

if accuracy2 > accuracy1:

    print("\nAccuracy Improved")

elif accuracy2 == accuracy1:

    print("\nAccuracy Remains Same")

else:

    print("\nAccuracy Decreased")