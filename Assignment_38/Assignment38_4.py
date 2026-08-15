import pandas as pd

Border = "-" * 50

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print(Border)
print("Distribution of FinalResult")
print(Border)

print(df["FinalResult"].value_counts())

print(Border)
print("Percentage")
print(Border)

Percentage = df["FinalResult"].value_counts(normalize=True) * 100

print(Percentage)

if abs(Percentage[1] - Percentage[0]) <= 10:
    print("\nDataset is Balanced")
else:
    print("\nDataset is Not Balanced")