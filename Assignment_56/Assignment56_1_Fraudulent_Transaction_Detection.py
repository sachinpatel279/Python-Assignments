import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (BaggingClassifier, RandomForestClassifier, AdaBoostClassifier, VotingClassifier)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, confusion_matrix)

Border = "-"*60

def FraudDetection(Filename):

    print(Border)
    print("---- Step 1 : Load the dataset ----")
    print(Border)

    df = pd.read_csv(Filename)

    print(df.head())
    print("Shape of dataset : ",df.shape)

    print(Border)
    print("---- Step 2 : Check the missing values ----")
    print(Border)    

    print(df.isnull().sum())

    print(Border)
    print("---- Step 3 : Separate the input and output variables ----")
    print(Border)    

    X = df.drop("Fraud", axis =1)
    Y = df["Fraud"]

    print("Independent variables :  ")
    print(X.head())

    print("Dependent variables : ")
    print(Y.head())

    print(Border)
    print("---- Split the dataset ----")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y , random_state=42, test_size=0.2, stratify=Y )

    print("Training data : ",X_train.shape)
    print("Testing data : ",X_test.shape)

    print(Border)
    print("---- Step 4 : Scaled the data ----")
    print(Border)    

    scaler =StandardScaler()

    train_scaled = scaler.fit_transform(X_train)
    test_scaled = scaler.transform(X_test)
    print("Data scalling completed")

    print(Border)
    print("---- Step 6 : Decision Tree Classifier ----")
    print(Border)    

    DT = DecisionTreeClassifier(random_state=42)

    DT.fit(X_train,Y_train)

    Y_pred_DT = DT.predict(X_test)

    Accuracy_DT = accuracy_score(Y_test, Y_pred_DT)
    Precision_DT = precision_score(Y_test, Y_pred_DT, zero_division=0)
    Recall_DT = recall_score(Y_test, Y_pred_DT, zero_division=0)
    F1_DT = f1_score(Y_test, Y_pred_DT, zero_division=0)
    CM_DT = confusion_matrix(Y_test, Y_pred_DT)

    print("Accuracy  : ", Accuracy_DT)
    print("Precision : ", Precision_DT)
    print("Recall    : ", Recall_DT)
    print("F1 Score  : ", F1_DT)

    print("Confusion Matrix : ")
    print(CM_DT)

    print(Border)
    print("---- Step 7 : Bagging Classifier ----")
    print(Border)

    Bagging = BaggingClassifier(
        estimator=DecisionTreeClassifier(random_state=42),
        n_estimators=10,
        random_state=42
    )

    Bagging.fit(X_train, Y_train)

    Y_pred_Bagging = Bagging.predict(X_test)

    Accuracy_Bagging = accuracy_score(Y_test, Y_pred_Bagging)
    Precision_Bagging = precision_score(Y_test, Y_pred_Bagging, zero_division=0)
    Recall_Bagging = recall_score(Y_test, Y_pred_Bagging, zero_division=0)
    F1_Bagging = f1_score(Y_test, Y_pred_Bagging, zero_division=0)
    CM_Bagging = confusion_matrix(Y_test, Y_pred_Bagging)

    print("Accuracy  : ", Accuracy_Bagging)
    print("Precision : ", Precision_Bagging)
    print("Recall    : ", Recall_Bagging)
    print("F1 Score  : ", F1_Bagging)

    print("Confusion Matrix : ")
    print(CM_Bagging)

    print(Border)
    print("----- Step 8 : Random Forest Classifier -----")
    print(Border)

    RF = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    RF.fit(X_train, Y_train)

    Y_pred_RF = RF.predict(X_test)

    Accuracy_RF = accuracy_score(Y_test, Y_pred_RF)
    Precision_RF = precision_score(Y_test, Y_pred_RF, zero_division=0)
    Recall_RF = recall_score(Y_test, Y_pred_RF, zero_division=0)
    F1_RF = f1_score(Y_test, Y_pred_RF, zero_division=0)
    CM_RF = confusion_matrix(Y_test, Y_pred_RF)

    print("Accuracy  : ", Accuracy_RF)
    print("Precision : ", Precision_RF)
    print("Recall    : ", Recall_RF)
    print("F1 Score  : ", F1_RF)

    print("Confusion Matrix : ")
    print(CM_RF)


    print(Border)
    print("----- Step 9 : AdaBoost Classifier -----")
    print(Border)

    AdaBoost = AdaBoostClassifier(n_estimators=50, random_state=42)

    AdaBoost.fit(X_train, Y_train)

    Y_pred_AdaBoost = AdaBoost.predict(X_test)

    Accuracy_AdaBoost = accuracy_score(Y_test, Y_pred_AdaBoost)
    Precision_AdaBoost = precision_score(Y_test, Y_pred_AdaBoost, zero_division=0)
    Recall_AdaBoost = recall_score(Y_test, Y_pred_AdaBoost, zero_division=0)
    F1_AdaBoost = f1_score(Y_test, Y_pred_AdaBoost, zero_division=0)
    CM_AdaBoost = confusion_matrix(Y_test, Y_pred_AdaBoost)

    print("Accuracy  : ", Accuracy_AdaBoost)
    print("Precision : ", Precision_AdaBoost)
    print("Recall    : ", Recall_AdaBoost)
    print("F1 Score  : ", F1_AdaBoost)

    print("Confusion Matrix : ")
    print(CM_AdaBoost)

    print(Border)
    print("----- Step 10 : Voting Classifier -----")
    print(Border)

    Voting = VotingClassifier(
        estimators=[
            ("LogisticRegression",LogisticRegression()),
            ("DecisionTree", DecisionTreeClassifier(random_state=42)),
            ("KNN", KNeighborsClassifier(n_neighbors=5))
        ],
        voting="hard"
    )

    Voting.fit(train_scaled, Y_train)

    Y_pred_Voting = Voting.predict(test_scaled)

    Accuracy_Voting = accuracy_score(Y_test, Y_pred_Voting)
    Precision_Voting = precision_score(Y_test, Y_pred_Voting, zero_division=0)
    Recall_Voting = recall_score(Y_test, Y_pred_Voting, zero_division=0)
    F1_Voting = f1_score(Y_test, Y_pred_Voting, zero_division=0)
    CM_Voting = confusion_matrix(Y_test, Y_pred_Voting)

    print("Accuracy  : ", Accuracy_Voting)
    print("Precision : ", Precision_Voting)
    print("Recall    : ", Recall_Voting)
    print("F1 Score  : ", F1_Voting)

    print("Confusion Matrix : ")
    print(CM_Voting)

    print(Border)
    print("----- Step 11 : Final Comparison -----")
    print(Border)

    Comparison = pd.DataFrame({
        "Algorithm": [
            "Decision Tree",
            "Bagging",
            "Random Forest",
            "AdaBoost",
            "Voting"
        ],

        "Accuracy": [
            Accuracy_DT,
            Accuracy_Bagging,
            Accuracy_RF,
            Accuracy_AdaBoost,
            Accuracy_Voting
        ],

        "Precision": [
            Precision_DT,
            Precision_Bagging,
            Precision_RF,
            Precision_AdaBoost,
            Precision_Voting
        ],

        "Recall": [
            Recall_DT,
            Recall_Bagging,
            Recall_RF,
            Recall_AdaBoost,
            Recall_Voting
        ],

        "F1 Score": [
            F1_DT,
            F1_Bagging,
            F1_RF,
            F1_AdaBoost,
            F1_Voting
        ]
    })

    print(Comparison.to_string(index=False))

    
def main():
    FraudDetection("Fraudulent_Transaction_Detection.csv")


if __name__ == "__main__":
    main()