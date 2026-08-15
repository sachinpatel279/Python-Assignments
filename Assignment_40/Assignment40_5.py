import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "-" * 50

print(Border)
print("Manual Accuracy Calculation")
print(Border)


df = pd.read_csv("student_performance_ml.csv")

print("Dataset Loaded Successfully")


X = df.drop(columns=["FinalResult"])

Y = df["FinalResult"]

# Split Dataset

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)


#Create and Train Model

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)


#  Prediction

Y_pred = model.predict(X_test)

#  Calculate Accuracy Manually

correct = 0

for actual, predicted in zip(Y_test, Y_pred):

    if actual == predicted:
        correct = correct + 1


total = len(Y_test)

manual_accuracy = correct / total

# Display Manual Accuracy

print("\nTotal Testing Students :", total)

print("Correct Predictions    :", correct)

print(
    "Manual Accuracy        :",
    round(manual_accuracy * 100, 2),
    "%"
)



# Verify With sklearn Accuracy

sklearn_accuracy = accuracy_score(
    Y_test,
    Y_pred
)

print(
    "Sklearn Accuracy       :",
    round(sklearn_accuracy * 100, 2),
    "%"
)


# Compare Both

if manual_accuracy == sklearn_accuracy:

    print("\nBoth Accuracy Values are Same")

else:

    print("\nAccuracy Values are Different")