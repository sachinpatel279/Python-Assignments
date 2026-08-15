import pandas as pd
import matplotlib.pyplot as plt

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

Passed = df[df["FinalResult"] == 1]
Failed = df[df["FinalResult"] == 0]

plt.figure(figsize=(7,5))

plt.scatter(Passed["AssignmentsCompleted"],
            Passed["FinalResult"],
            color="green",
            label="Pass")

plt.scatter(Failed["AssignmentsCompleted"],
            Failed["FinalResult"],
            color="red",
            label="Fail")

plt.title("AssignmentsCompleted vs FinalResult")

plt.xlabel("Assignments Completed")
plt.ylabel("FinalResult")

plt.legend()

plt.show()