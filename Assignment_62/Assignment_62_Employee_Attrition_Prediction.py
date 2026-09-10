import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix,classification_report, ConfusionMatrixDisplay)


# ---------------------------------------------------------
# 1. Load the dataset
# ---------------------------------------------------------

def LoadData():
    df = pd.read_csv("Employee_Attrition.csv")
    return df


# ---------------------------------------------------------
# 2. Display dataset information
# ---------------------------------------------------------

def DisplayDatasetInformation(df):
    print("\nShape of dataset:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nFirst five records:")
    print(df.head())

    print("\nMissing values:")
    print(df.isnull().sum())


# ---------------------------------------------------------
# 3. Identify numerical and categorical features
# ---------------------------------------------------------

def IdentifyFeatures(df):
    numerical_features = [
        "Age",
        "MonthlyIncome",
        "YearsAtCompany",
        "TotalWorkingYears",
        "DistanceFromHome",
        "JobSatisfaction",
        "WorkLifeBalance",
        "NumCompaniesWorked",
        "TrainingTimesLastYear"
    ]

    categorical_features = [
        "OverTime"
    ]

    print("\nNumerical Features:")
    print(numerical_features)

    print("\nCategorical Features:")
    print(categorical_features)

    return numerical_features, categorical_features


# ---------------------------------------------------------
# 4. Prepare independent and dependent variables
# ---------------------------------------------------------

def PrepareData(df):
    # Convert target:
    # No  -> 0
    # Yes -> 1
    df["Attrition"] = df["Attrition"].map({
        "No": 0,
        "Yes": 1
    })

    X = df.drop("Attrition", axis=1)
    y = df["Attrition"]

    return X, y


# ---------------------------------------------------------
# 5. Create preprocessing and MLP model
# ---------------------------------------------------------

def CreateModel(numerical_features, categorical_features):

    # Numerical features are scaled.
    # Categorical features are converted using OneHotEncoder.
    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numerical",
                StandardScaler(),
                numerical_features
            ),
            (
                "categorical",
                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=False
                ),
                categorical_features
            )
        ]
    )

    # MLP contains two hidden layers:
    # First hidden layer  = 16 neurons
    # Second hidden layer = 8 neurons
    mlp = MLPClassifier(
        hidden_layer_sizes=(16, 8),
        activation="relu",
        solver="adam",
        learning_rate_init=0.001,
        max_iter=1000,
        random_state=42,
        early_stopping=False
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("mlp", mlp)
        ]
    )

    return model


# ---------------------------------------------------------
# 6. Predict attrition for a new employee
# ---------------------------------------------------------

def PredictAttrition(employee_data, model):

    employee_df = pd.DataFrame(
        [employee_data]
    )

    prediction = model.predict(employee_df)[0]
    probability = model.predict_proba(employee_df)[0][1]

    if prediction == 1:
        result = "Employee is likely to leave"
    else:
        result = "Employee is likely to stay"

    print("\nEmployee Information:")
    print(employee_df)

    print("\nPrediction:")
    print(prediction)

    print("Result:")
    print(result)

    print("Probability of leaving: {:.2f}%".format(
        probability * 100
    ))

    return prediction


# ---------------------------------------------------------
# 7. Main function
# ---------------------------------------------------------

def main():

    # Task 1: Load dataset
    df = LoadData()

    # Tasks 2 and 3: Display information
    DisplayDatasetInformation(df)

    # Task 4: Identify features
    numerical_features, categorical_features = IdentifyFeatures(df)

    # Tasks 5, 6 and 7: Prepare data
    X, y = PrepareData(df)

    print("\nIndependent variables:")
    print(X.head())

    print("\nDependent variable:")
    print(y.head())

    print("\nTarget distribution:")
    print(y.value_counts())

    # Task 8: Divide data into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("\nTraining records:", X_train.shape[0])
    print("Testing records:", X_test.shape[0])

    # Tasks 9 and 10: Scaling and MLP design
    model = CreateModel(
        numerical_features,
        categorical_features
    )

    # Task 11: Train the network
    model.fit(X_train, y_train)

    # Task 12: Display number of iterations
    mlp = model.named_steps["mlp"]

    print("\nNumber of iterations required:")
    print(mlp.n_iter_)

    print("\nFinal training loss:")
    print(mlp.loss_)

    # Task 13: Training accuracy
    train_prediction = model.predict(X_train)

    train_accuracy = accuracy_score(
        y_train,
        train_prediction
    )

    print("\nTraining Accuracy:")
    print("{:.2f}%".format(train_accuracy * 100))

    # Task 14: Testing accuracy
    test_prediction = model.predict(X_test)

    test_accuracy = accuracy_score(
        y_test,
        test_prediction
    )

    print("\nTesting Accuracy:")
    print("{:.2f}%".format(test_accuracy * 100))

    # Additional evaluation
    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            test_prediction,
            target_names=[
                "Stay",
                "Leave"
            ],
            zero_division=0
        )
    )

    # Task 15: Confusion matrix
    cm = confusion_matrix(
        y_test,
        test_prediction
    )

    print("\nConfusion Matrix:")
    print(cm)

    ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Stay", "Leave"]
    ).plot()

    plt.title("Employee Attrition Confusion Matrix")
    plt.show()

    # Task 16: Plot loss curve
    plt.figure(figsize=(8, 5))

    plt.plot(
        mlp.loss_curve_,
        label="Training Loss"
    )

    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.title("MLP Training Loss Curve")
    plt.legend()
    plt.grid()
    plt.show()

    # Task 17 and 18: Test five new employee records
    employee_1 = {
        "Age": 25,
        "MonthlyIncome": 2200,
        "YearsAtCompany": 1,
        "TotalWorkingYears": 2,
        "DistanceFromHome": 20,
        "JobSatisfaction": 2,
        "WorkLifeBalance": 2,
        "OverTime": "Yes",
        "NumCompaniesWorked": 2,
        "TrainingTimesLastYear": 2
    }

    employee_2 = {
        "Age": 45,
        "MonthlyIncome": 8500,
        "YearsAtCompany": 12,
        "TotalWorkingYears": 20,
        "DistanceFromHome": 5,
        "JobSatisfaction": 4,
        "WorkLifeBalance": 4,
        "OverTime": "No",
        "NumCompaniesWorked": 2,
        "TrainingTimesLastYear": 4
    }

    employee_3 = {
        "Age": 29,
        "MonthlyIncome": 3000,
        "YearsAtCompany": 2,
        "TotalWorkingYears": 5,
        "DistanceFromHome": 25,
        "JobSatisfaction": 2,
        "WorkLifeBalance": 2,
        "OverTime": "Yes",
        "NumCompaniesWorked": 4,
        "TrainingTimesLastYear": 1
    }

    employee_4 = {
        "Age": 38,
        "MonthlyIncome": 6500,
        "YearsAtCompany": 8,
        "TotalWorkingYears": 12,
        "DistanceFromHome": 4,
        "JobSatisfaction": 4,
        "WorkLifeBalance": 3,
        "OverTime": "No",
        "NumCompaniesWorked": 1,
        "TrainingTimesLastYear": 3
    }

    employee_5 = {
        "Age": 31,
        "MonthlyIncome": 2800,
        "YearsAtCompany": 1,
        "TotalWorkingYears": 6,
        "DistanceFromHome": 18,
        "JobSatisfaction": 1,
        "WorkLifeBalance": 2,
        "OverTime": "Yes",
        "NumCompaniesWorked": 5,
        "TrainingTimesLastYear": 2
    }

    print("\n========== New Employee Predictions ==========")

    PredictAttrition(employee_1, model)
    PredictAttrition(employee_2, model)
    PredictAttrition(employee_3, model)
    PredictAttrition(employee_4, model)
    PredictAttrition(employee_5, model)


if __name__ == "__main__":
    main()