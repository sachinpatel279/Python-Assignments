import pandas as pd

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Average values grouped by FinalResult\n")

print(df.groupby("FinalResult")[["StudyHours","Attendance"]].mean())