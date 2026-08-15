import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = "-" * 50

print(Border)
print("Misclassified Students")
print(Border)


df = pd.read_csv("student_performance_ml.csv")

print("Dataset Loaded Successfully")


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

model.fit(
    X_train,
    Y_train
)


Y_pred = model.predict(X_test)


result = X_test.copy()

result["Actual"] = Y_test.values

result["Predicted"] = Y_pred


misclassified = result[
    result["Actual"] != result["Predicted"]
]


print("\nMisclassified Students:")

print(misclassified)

count = len(misclassified)

print(
    "\nTotal Misclassified Students :",
    count
)


if count > 0:

    print("\nCommon Pattern:")

    print(
        "Misclassified students usually have feature "
        "values close to the decision boundary."
    )

else:

    print(
        "\nNo students are misclassified."
    )