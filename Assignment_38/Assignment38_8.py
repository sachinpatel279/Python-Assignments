import pandas as pd
import matplotlib.pyplot as plt

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

plt.figure(figsize=(6,5))

plt.boxplot(df["Attendance"])

plt.title("Attendance Boxplot")

plt.ylabel("Attendance")

plt.show()