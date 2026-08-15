import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = "-" * 50

print(Border)
print("Prediction for 5 New Students")
print(Border)

df = pd.read_csv("student_performance_ml.csv")


X = df[
    [
        "StudyHours",
        "Attendance"
    ]
]

Y = df["FinalResult"]

# Split Dataset


X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)


model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

new_students = pd.DataFrame(
    {
        "StudyHours": [
            2,
            4,
            6,
            8,
            10
        ],

        "Attendance": [
            60,
            70,
            80,
            90,
            95
        ]
    }
)


prediction = model.predict(new_students)

new_students["PredictedResult"] = prediction

print("\nPrediction Results")

print(new_students)