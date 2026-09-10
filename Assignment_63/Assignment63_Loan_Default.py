import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
    ConfusionMatrixDisplay
)


# ---------------------------------------------------------
# 1. Load the dataset
# ---------------------------------------------------------

def LoadData():

    df = pd.read_csv("Loan_Default.csv")

    return df


# ---------------------------------------------------------
# 2. Exploratory Data Analysis
# ---------------------------------------------------------

def ExploreData(df):

    print("\nShape of Dataset:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nFirst Five Records:")
    print(df.head())

    print("\nDataset Information:")
    print(df.info())

    print("\nStatistical Information:")
    print(df.describe())

    print("\nTarget Distribution:")
    print(df["Default"].value_counts())


# ---------------------------------------------------------
# 3. Find Missing Values
# ---------------------------------------------------------

def CheckMissingValues(df):

    print("\nMissing Values:")
    print(df.isnull().sum())


# ---------------------------------------------------------
# 4. Check Target Class Balance
# ---------------------------------------------------------

def CheckClassBalance(df):

    print("\nDefault Class Distribution:")
    print(df["Default"].value_counts())

    print("\nDefault Class Percentage:")
    print(df["Default"].value_counts(normalize=True) * 100)


# ---------------------------------------------------------
# 5. Identify Numerical and Categorical Features
# ---------------------------------------------------------

def IdentifyFeatures(df):

    numerical_features = [
        "Age",
        "Income",
        "LoanAmount",
        "CreditScore",
        "EmploymentYears",
        "ExistingLoans",
        "MonthlyDebt",
        "LoanTerm"
    ]

    categorical_features = [
        "PreviousDefault",
        "HomeOwnership"
    ]

    print("\nNumerical Features:")
    print(numerical_features)

    print("\nCategorical Features:")
    print(categorical_features)

    return numerical_features, categorical_features


# ---------------------------------------------------------
# 6. Separate X and y
# ---------------------------------------------------------

def PrepareData(df):

    # Convert PreviousDefault
    df["PreviousDefault"] = df["PreviousDefault"].map({
        "No": 0,
        "Yes": 1
    })

    X = df.drop("Default", axis=1)

    y = df["Default"]

    return X, y


# ---------------------------------------------------------
# 7. Create MLP Model
# ---------------------------------------------------------

def CreateModel(numerical_features, categorical_features):

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

    mlp = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
        )

    model = Pipeline(
        steps=[("preprocessor", preprocessor), ("mlp", mlp)])

    return model


# ---------------------------------------------------------
# 8. Train Model
# ---------------------------------------------------------

def TrainModel(model, X_train, Y_train):

    model.fit(X_train, Y_train)

    return model


# ---------------------------------------------------------
# 9. Calculate Accuracy
# ---------------------------------------------------------

def CalculateAccuracy(model, X_test, Y_test):

    prediction = model.predict(X_test)

    accuracy = accuracy_score(
        Y_test,
        prediction
    )

    print("\nAccuracy:")
    print("{:.2f}%".format(accuracy * 100))

    return prediction


# ---------------------------------------------------------
# 10. Confusion Matrix
# ---------------------------------------------------------

def DisplayConfusionMatrix(Y_test, prediction):

    cm = confusion_matrix(
        Y_test,
        prediction
    )

    print("\nConfusion Matrix:")
    print(cm)

    ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=[
            "Low Default Risk",
            "High Default Risk"
        ]
    ).plot()

    plt.title("Loan Default Confusion Matrix")

    plt.show()


# ---------------------------------------------------------
# 11. Classification Report
# ---------------------------------------------------------

def DisplayClassificationReport(Y_test, prediction):

    print("\nClassification Report:")

    print(
        classification_report(
            Y_test,
            prediction,
            target_names=[
                "Low Default Risk",
                "High Default Risk"
            ],
            zero_division=0
        )
    )


# ---------------------------------------------------------
# 12. Calculate Precision, Recall and F1 Score
# ---------------------------------------------------------

def CalculateMetrics(Y_test, prediction):

    precision = precision_score(Y_test, prediction, zero_division=0)

    recall = recall_score(Y_test, prediction, zero_division=0)

    f1 = f1_score(Y_test, prediction, zero_division=0)

    print("\nPrecision:")
    print("{:.2f}%".format(precision * 100))

    print("\nRecall:")
    print("{:.2f}%".format(recall * 100))

    print("\nF1 Score:")
    print("{:.2f}%".format(f1 * 100))


# ---------------------------------------------------------
# 13. Plot Training Loss
# ---------------------------------------------------------

def PlotLossCurve(model):

    mlp = model.named_steps["mlp"]

    print("\nNumber of Iterations:")
    print(mlp.n_iter_)

    print("\nFinal Training Loss:")
    print(mlp.loss_)

    plt.figure(figsize=(8, 5))

    plt.plot(mlp.loss_curve_, label="Training Loss")

    plt.xlabel("Iterations")
    plt.ylabel("Loss")

    plt.title("MLP Training Loss Curve")

    plt.legend()

    plt.grid()

    plt.show()


# ---------------------------------------------------------
# 14. Predict New Loan Applicant
# ---------------------------------------------------------

def PredictLoan(applicant, model):

    applicant_df = pd.DataFrame([applicant])

    prediction = model.predict(applicant_df)[0]

    probability = model.predict_proba(applicant_df)[0][1]

    print("\nApplicant Information:")
    print(applicant_df)

    print("\nPrediction:")

    if prediction == 1:

        print("1 -> High default risk")

    else:

        print("0 -> Low default risk")

    print("\nProbability of High Default Risk:")

    print("{:.2f}%".format(probability * 100))


# ---------------------------------------------------------
# 15. Main Function
# ---------------------------------------------------------

def main():

    # Task 1:
    # Load Dataset

    df = LoadData()


    # Task 2:
    # Exploratory Analysis
    ExploreData(df)


    # Task 3:
    # Missing Values
    CheckMissingValues(df)


    # Task 4:
    # Check Class Balance
    CheckClassBalance(df)


    # Task 5:
    # Identify Features
    numerical_features, categorical_features = IdentifyFeatures(df)


    # Task 6:
    # Separate X and y
    X, y = PrepareData(df)


    print("\nIndependent Variables:")
    print(X.head())


    print("\nDependent Variable:")
    print(y.head())


    # Task 7:
    # Train Test Split
    X_train, X_test, Y_train, Y_test = train_test_split(X ,y, test_size=0.2, random_state=42, stratify=y)


    print("\nTraining Records:")
    print(X_train.shape[0])


    print("\nTesting Records:")
    print(X_test.shape[0])


    # Task 8:
    # Stratified splitting

    print("\nStratified Splitting:")

    print(
        "Stratified splitting should be used because "
        "it maintains the same proportion of Default classes "
        "in training and testing datasets."
    )


    # Task 9 and 10:
    # Scaling and MLP

    model = CreateModel(numerical_features, categorical_features)

    # Task 11:
    # Train Model
    model = TrainModel(model, X_train, Y_train)


    # Task 12:
    # Accuracy
    prediction = CalculateAccuracy(model, X_test, Y_test)


    # Task 13:
    # Confusion Matrix
    DisplayConfusionMatrix(Y_test, prediction)


    # Task 14:
    # Classification Report
    DisplayClassificationReport(Y_test, prediction)


    # Task 15:
    # Precision Recall F1
    CalculateMetrics(Y_test, prediction)


    # Task 16:
    # Training Loss
    PlotLossCurve(model)


    # -----------------------------------------------------
    # Task 17:
    # Test New Loan Applicants
    # -----------------------------------------------------
    applicant_1 = {
        "Age": 25,
        "Income": 30000,
        "LoanAmount": 15000,
        "CreditScore": 620,
        "EmploymentYears": 2,
        "ExistingLoans": 2,
        "MonthlyDebt": 1200,
        "LoanTerm": 60,
        "PreviousDefault": "Yes",
        "HomeOwnership": "Rent"
    }


    applicant_2 = {

        "Age": 45,
        "Income": 90000,
        "LoanAmount": 20000,
        "CreditScore": 780,
        "EmploymentYears": 15,
        "ExistingLoans": 1,
        "MonthlyDebt": 800,
        "LoanTerm": 36,
        "PreviousDefault": "No",
        "HomeOwnership": "Own"
    }


    applicant_3 = {

        "Age": 30,
        "Income": 40000,
        "LoanAmount": 35000,
        "CreditScore": 580,
        "EmploymentYears": 3,
        "ExistingLoans": 4,
        "MonthlyDebt": 2500,
        "LoanTerm": 60,
        "PreviousDefault": "Yes",
        "HomeOwnership": "Rent"
    }


    applicant_4 = {

        "Age": 38,
        "Income": 70000,
        "LoanAmount": 25000,
        "CreditScore": 720,
        "EmploymentYears": 10,
        "ExistingLoans": 1,
        "MonthlyDebt": 900,
        "LoanTerm": 36,
        "PreviousDefault": "No",
        "HomeOwnership": "Mortgage"
    }


    applicant_5 = {

        "Age": 29,
        "Income": 35000,
        "LoanAmount": 30000,
        "CreditScore": 590,
        "EmploymentYears": 2,
        "ExistingLoans": 3,
        "MonthlyDebt": 2200,
        "LoanTerm": 60,
        "PreviousDefault": "Yes",
        "HomeOwnership": "Rent"
    }


    print("\n========== New Loan Applicant Predictions ==========")


    PredictLoan(applicant_1, model)


    PredictLoan(applicant_2, model)


    PredictLoan(applicant_3, model)


    PredictLoan(applicant_4, model)


    PredictLoan(applicant_5, model)

# ---------------------------------------------------------
# Program Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":

    main()