import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (accuracy_score, confusion_matrix, classification_report)


def BreastCancerPrediction(DataPath):

    Border = "-" * 50

    # ------------------------------------------------
    # Step 1 : Load Dataset
    # ------------------------------------------------

    print(Border)
    print("Step 1 : Load Dataset")
    print(Border)

    df = pd.read_csv(DataPath)

    print(df.head())

    print("\nDataset Shape : ", df.shape)


    # ------------------------------------------------
    # Step 2 : Remove Unwanted Column
    # ------------------------------------------------

    print(Border)
    print("Step 2 : Remove Unwanted Column")
    print(Border)

    if "CodeNumber" in df.columns:
        df = df.drop(columns=["CodeNumber"])

    print(df.head())


    # ------------------------------------------------
    # Step 3 : Handle Missing Values
    # ------------------------------------------------

    print(Border)
    print("Step 3 : Handle Missing Values")
    print(Border)

    print("\nMissing Values Before Cleaning :")
    print(df.isnull().sum())

    # Convert BareNuclei to numeric
    df["BareNuclei"] = pd.to_numeric(df["BareNuclei"],errors="coerce")

    print("\nMissing Values After Conversion :")
    print(df.isnull().sum())

    # Replace missing values with median
    df["BareNuclei"] = df["BareNuclei"].fillna(df["BareNuclei"].median())

    print("\nMissing Values After Cleaning :")
    print(df.isnull().sum())


    # ------------------------------------------------
    # Step 4 : Summary Statistics
    # ------------------------------------------------

    print(Border)
    print("Step 4 : Summary Statistics")
    print(Border)

    print(df.describe())


    # ------------------------------------------------
    # Step 5 : Correlation
    # ------------------------------------------------

    print(Border)
    print("Step 5 : Feature Correlation")
    print(Border)

    Correlation = df.corr()

    print(Correlation)

    plt.figure(figsize=(10, 8))

    plt.imshow(Correlation, cmap="coolwarm", interpolation="nearest")

    plt.colorbar()

    plt.xticks(range(len(Correlation.columns)), Correlation.columns, rotation=90)

    plt.yticks(range(len(Correlation.columns)),Correlation.columns)

    plt.title("Breast Cancer Feature Correlation")

    plt.tight_layout()

    plt.show()


    # ------------------------------------------------
    # Step 6 : Separate Independent and Dependent
    # Variables
    # ------------------------------------------------

    print(Border)
    print("Step 6 : Separate Independent and Dependent Variables")
    print(Border)

    X = df.drop("CancerType", axis=1)

    Y = df["CancerType"]

    print("Independent Variables :")
    print(X.head())

    print("\nDependent Variable :")
    print(Y.head())


    # ------------------------------------------------
    # Step 7 : Convert Target
    # ------------------------------------------------

    # Dataset:
    # 2 = Benign
    # 4 = Malignant

    Y = Y.map({
        2: 0,
        4: 1
    })

    print("\nTarget after conversion :")
    print(Y.value_counts())

    # 0 = Benign
    # 1 = Malignant


    # ------------------------------------------------
    # Step 8 : Split Dataset
    # ------------------------------------------------

    print(Border)
    print("Step 7 : Split Dataset")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("Training Data : ", X_train.shape)
    print("Testing Data  : ", X_test.shape)


    # ------------------------------------------------
    # Step 9 : Feature Scaling
    # ------------------------------------------------

    print(Border)
    print("Step 8 : Feature Scaling")
    print(Border)

    Scaler = StandardScaler()

    X_train = Scaler.fit_transform(X_train)

    X_test = Scaler.transform(X_test)

    print("Feature Scaling Completed Successfully.")


    # ------------------------------------------------
    # Step 10 : Create and Train Model
    # ------------------------------------------------

    print(Border)
    print("Step 9 : Create and Train Model")
    print(Border)

    Model = LogisticRegression(
        max_iter=10000
    )

    Model.fit(X_train, Y_train)

    print("Model Trained Successfully.")


    # ------------------------------------------------
    # Step 11 : Test Model
    # ------------------------------------------------

    print(Border)
    print("Step 10 : Test Model")   
    print(Border)

    Y_pred = Model.predict(X_test)

    print("Predicted Values :")
    print(Y_pred)


    # ------------------------------------------------
    # Step 12 : Accuracy
    # ------------------------------------------------

    print(Border)
    print("Step 11 : Accuracy")
    print(Border)

    Accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy :", Accuracy)

    print("Accuracy Percentage :",Accuracy * 100,"%")

    # ------------------------------------------------
    # Step 13 : Confusion Matrix
    # ------------------------------------------------

    print(Border)
    print("Step 12 : Confusion Matrix")
    print(Border)

    CM = confusion_matrix(Y_test, Y_pred)

    print(CM)


    # ------------------------------------------------
    # Step 14 : Classification Report
    # ------------------------------------------------

    print(Border)
    print("Step 13 : Classification Report")
    print(Border)

    Report = classification_report(
        Y_test,
        Y_pred,
        target_names=[
            "Benign",
            "Malignant"
        ]
    )

    print(Report)


    # ------------------------------------------------
    # Step 15 : Display Confusion Matrix
    # ------------------------------------------------

    plt.figure(figsize=(6, 5))

    plt.imshow(
        CM,
        cmap="Blues",
        interpolation="nearest"
    )

    plt.title("Confusion Matrix")

    plt.colorbar()

    Labels = [
        "Benign",
        "Malignant"
    ]

    plt.xticks(
        [0, 1],
        Labels
    )

    plt.yticks(
        [0, 1],
        Labels
    )

    plt.xlabel("Predicted")

    plt.ylabel("Actual")

    for i in range(CM.shape[0]):

        for j in range(CM.shape[1]):

            plt.text(
                j,
                i,
                CM[i, j],
                ha="center",
                va="center"
            )

    plt.tight_layout()
    plt.show()


def main():

    BreastCancerPrediction("breast-cancer-wisconsin.csv")

if __name__ == "__main__":
    main()