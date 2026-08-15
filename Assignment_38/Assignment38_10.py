import pandas as pd
import matplotlib.pyplot as plt

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

Passed = df[df["FinalResult"] == 1]
Failed = df[df["FinalResult"] == 0]

plt.figure(figsize=(7,5))

plt.scatter(Passed["SleepHours"],
            Passed["FinalResult"],
            color="green",
            label="Pass")

plt.scatter(Failed["SleepHours"],
            Failed["FinalResult"],
            color="red",
            label="Fail")

plt.title("SleepHours vs FinalResult")

plt.xlabel("Sleep Hours")
plt.ylabel("FinalResult")

plt.yticks([0, 1], ["Fail", "Pass"])

plt.legend()

plt.show()