import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

Student = pd.DataFrame({
    "StudyHours": [6],
    "Attendance": [85],
    "PreviousScore": [66],
    "AssignmentsCompleted": [7],
    "SleepHours": [7]
})

Prediction = model.predict(Student)

print(Border)
print("Prediction")
print(Border)

if Prediction[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")