import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

Border = "-"*60

def CustomerLoanApproval(FileName):

    print(Border)
    print("----- Step 1 : Load the dataset -----")
    print(Border)

    df = pd.read_csv(FileName)
    print(df.head())
    print("Shape of dataset : ",df.shape)


    print(Border)
    print("----- Step 2 : Check the missing values -----")
    print(Border)

    print(df.isnull().sum())


    print(Border)
    print("----- Step 3 : Separate input and output variables -----")
    print(Border)

    X = df.drop("LoanApproved", axis=1)
    Y = df["LoanApproved"]

    print("Independent Variables : ")
    print(X.head())

    print("Dependent Variables : ")
    print(Y.head())

    print(Border)
    print("----- Step 4 : Split the dataset -----")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, stratify=Y)
    print("Training Data : ",X.shape)
    print("Testing Data : ",Y.shape)


    print(Border)
    print("----- Step 5 : Scaled the data -----")
    print(Border)

    scaler = StandardScaler()

    train_scaled = scaler.fit_transform(X_train)
    test_scaled = scaler.transform(X_test)

    print("data scaling Completed")

    print(Border)
    print("----- Step 6 : Train model in Logistic Regression -----")
    print(Border)

    LR = LogisticRegression()

    LR.fit(train_scaled,Y_train)

    LR_Y_pred = LR.predict(test_scaled)
    LR_accuracy = accuracy_score(Y_test,LR_Y_pred)

    print("Logistic Regression Accuracy : ",LR_accuracy)

    
    print(Border)
    print("----- Step 7 : Train model in Decison Tree -----")
    print(Border)

    DT = DecisionTreeClassifier()
    DT.fit(X_train, Y_train)

    DT_Y_pred = DT.predict(X_test)
    DT_accuracy = accuracy_score(Y_test,DT_Y_pred)

    print("Decision tree Accuracy : ",DT_accuracy)

    
    print(Border)
    print("----- Step 8 : Train model in KNN -----")
    print(Border)

    KNN = KNeighborsClassifier(n_neighbors=5)
    KNN.fit(train_scaled,Y_train)

    KNN_Y_pred = KNN.predict(test_scaled)
    KNN_accuracy = accuracy_score(Y_test,KNN_Y_pred)

    print("KNN accuracy : ",KNN_accuracy)

    
    print(Border)
    print("----- Step 9 : Hard Voting -----")
    print(Border)

    hard_vote = VotingClassifier(
            estimators=[
                ("LogisticRegression", LogisticRegression()),
                ("DecisonTree", DecisionTreeClassifier(random_state=42)),
                ("KNN", KNeighborsClassifier(n_neighbors=5))
            ],
            voting="hard"
        )

    hard_vote.fit(train_scaled, Y_train)
    Hard__Y_pred = hard_vote.predict(test_scaled)
    hard_accuracy = accuracy_score(Y_test,Hard__Y_pred)
    print("hard voting accuracy : ",hard_accuracy)


    print(Border)
    print("----- Step 10 : Soft Voting -----")
    print(Border)

    soft_vote = VotingClassifier(
                    estimators=[
                ("LogisticRegression", LogisticRegression()),
                ("DecisonTree", DecisionTreeClassifier(random_state=42)),
                ("KNN", KNeighborsClassifier(n_neighbors=5))
            ],
            voting="soft"
        )

    soft_vote.fit(train_scaled, Y_train)
    Soft__Y_pred = soft_vote.predict(test_scaled)
    soft_accuracy = accuracy_score(Y_test,Soft__Y_pred)
    print("soft voting accuracy : ",soft_accuracy)

    print(Border)
    print("----- Step 11 : Compare Accuracy Score -----")
    print(Border)

    print("Logistic Regression : ",LR_accuracy)
    print("Decision Tree : ",DT_accuracy)
    print("KNN : ",KNN_accuracy)
    print("Hard Voting : ",hard_accuracy)
    print("Soft Voting : ",soft_accuracy)


def main():
    CustomerLoanApproval("Customer_Loan_Approval.csv")


if __name__ =="__main__":
    main()