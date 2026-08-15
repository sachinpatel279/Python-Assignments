
import pandas as pd

Border = "-" * 50

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print(Border)
print("Student Statistics")
print(Border)

print("Total Students :", len(df))

Passed = (df["FinalResult"] == 1).sum()
Failed = (df["FinalResult"] == 0).sum()

print("Passed Students :", Passed)
print("Failed Students :", Failed)