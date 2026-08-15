import pandas as pd
import matplotlib.pyplot as plt

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

plt.figure(figsize=(7,5))

plt.hist(df["StudyHours"], bins=6)

plt.title("Histogram of StudyHours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")

plt.show()