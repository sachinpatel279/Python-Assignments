import pandas as pd

Border = "-" * 50

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print(Border)
print("Dataset Statistics")
print(Border)

print("Average Study Hours :", df["StudyHours"].mean())

print("Average Attendance :", df["Attendance"].mean())

print("Maximum Previous Score :", df["PreviousScore"].max())

print("Minimum Sleep Hours :", df["SleepHours"].min())