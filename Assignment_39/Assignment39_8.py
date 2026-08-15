import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

Border = "-" * 50

def main():

    ####################################################
    # Step 1 : Load Dataset
    ####################################################

    print(Border)
    print("Step 1 : Load Dataset")
    print(Border)

    DataPath = "student_performance_ml.csv"

    df = pd.read_csv(DataPath)

    print("Dataset Loaded Successfully")

    ####################################################
    # Step 2 : Data Analysis
    ####################################################

    print(Border)
    print("Step 2 : Data Analysis")
    print(Border)

    print("First 5 Records")
    print(df.head())

    print("\nLast 5 Records")
    print(df.tail())

    print("\nDataset Shape :", df.shape)

    print("\nColumn Names")
    print(df.columns)

    print("\nData Types")
    print(df.dtypes)

    print("\nTotal Students :", len(df))

    print("\nPass and Fail Count")
    print(df["FinalResult"].value_counts())

    print("\nAverage Study Hours :", df["StudyHours"].mean())
    print("Average Attendance :", df["Attendance"].mean())
    print("Maximum Previous Score :", df["PreviousScore"].max())
    print("Minimum Sleep Hours :", df["SleepHours"].min())

    ####################################################
    # Step 3 : Visualization
    ####################################################

    print(Border)
    print("Step 3 : Visualization")
    print(Border)

    # Histogram

    plt.figure(figsize=(6,5))

    plt.hist(df["StudyHours"], bins=6)

    plt.title("Histogram of StudyHours")
    plt.xlabel("Study Hours")
    plt.ylabel("Frequency")

    plt.show()

    # Scatter Plot

    Passed = df[df["FinalResult"] == 1]
    Failed = df[df["FinalResult"] == 0]

    plt.figure(figsize=(6,5))

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

    # Boxplot

    plt.figure(figsize=(5,5))

    plt.boxplot(df["Attendance"])

    plt.title("Attendance Boxplot")

    plt.show()

    ####################################################
    # Step 4 : Train Test Split
    ####################################################

    print(Border)
    print("Step 4 : Train Test Split")
    print(Border)

    X = df.drop("FinalResult", axis=1)

    y = df["FinalResult"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Training Records :", len(X_train))
    print("Testing Records :", len(X_test))

    ####################################################
    # Step 5 : Model Training
    ####################################################

    print(Border)
    print("Step 5 : Model Training")
    print(Border)

    model = DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )

    model.fit(X_train, y_train)

    print("Model Trained Successfully")

    ####################################################
    # Step 6 : Prediction
    ####################################################

    print(Border)
    print("Step 6 : Prediction")
    print(Border)

    y_pred = model.predict(X_test)

    Result = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": y_pred
    })

    print(Result)

    ####################################################
    # Predict New Student
    ####################################################

    Student = pd.DataFrame({
        "StudyHours":[6],
        "Attendance":[85],
        "PreviousScore":[66],
        "AssignmentsCompleted":[7],
        "SleepHours":[7]
    })

    Prediction = model.predict(Student)

    if Prediction[0] == 1:
        print("\nNew Student : PASS")
    else:
        print("\nNew Student : FAIL")

    ####################################################
    # Step 7 : Accuracy
    ####################################################

    print(Border)
    print("Step 7 : Accuracy")
    print(Border)

    TrainPrediction = model.predict(X_train)

    TrainingAccuracy = accuracy_score(
        y_train,
        TrainPrediction
    )

    TestingAccuracy = accuracy_score(
        y_test,
        y_pred
    )

    print("Training Accuracy :", TrainingAccuracy * 100,"%")
    print("Testing Accuracy :", TestingAccuracy * 100,"%")

    ####################################################
    # Step 8 : Confusion Matrix
    ####################################################

    print(Border)
    print("Step 8 : Confusion Matrix")
    print(Border)

    cm = confusion_matrix(y_test, y_pred)

    print(cm)

    TN, FP, FN, TP = cm.ravel()

    print("True Negative :", TN)
    print("False Positive :", FP)
    print("False Negative :", FN)
    print("True Positive :", TP)

    Display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Fail","Pass"]
    )

    Display.plot()

    plt.title("Confusion Matrix")

    plt.show()

    ####################################################
    # Step 9 : Final Conclusion
    ####################################################

    print(Border)
    print("Step 9 : Final Conclusion")
    print(Border)

    if TrainingAccuracy - TestingAccuracy > 0.10:
        print("Model is Overfitting")

    elif TrainingAccuracy < 0.70 and TestingAccuracy < 0.70:
        print("Model is Underfitting")

    else:
        print("Model is Performing Well")



if __name__ == "__main__":
    main()