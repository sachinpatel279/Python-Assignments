import pandas as pd
import matplotlib.pyplot as plt

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

Passed = df[df["FinalResult"] == 1]
Failed = df[df["FinalResult"] == 0]

plt.figure(figsize=(7,5))

plt.scatter(Passed["StudyHours"],
            Passed["PreviousScore"],
            color="green",
            label="Pass")

plt.scatter(Failed["StudyHours"],
            Failed["PreviousScore"],
            color="red",
            label="Fail")

plt.title("StudyHours vs PreviousScore")

plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")

plt.legend()

plt.show()