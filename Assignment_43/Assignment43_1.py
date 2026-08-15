import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


###################################################
# Function Name : CheckAccuracy
# Description   : Calculate accuracy of KNN
###################################################

def CheckAccuracy(X, Y):

    Border = "-" * 40

    print(Border)
    print("Accuracy Calculation")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    for K in range(1, 6):

        Model = KNeighborsClassifier(n_neighbors=K)

        Model.fit(X_train, Y_train)

        Y_pred = Model.predict(X_test)

        Accuracy = accuracy_score(Y_test, Y_pred)

        print("Accuracy for K =", K, "is :", Accuracy * 100, "%")


###################################################
# Main Function
###################################################

def main():

    Border = "-" * 40

    ###################################################
    # Step 1 : Get Data
    ###################################################

    print(Border)
    print("Step 1 : Get Data")
    print(Border)

    DataPath = "PlayPredictor.csv"

    Dataset = pd.read_csv(DataPath)

    print("Dataset loaded successfully")

    print(Dataset)


    ###################################################
    # Remove unwanted first column
    ###################################################

    Dataset.drop("Unnamed: 0", axis=1, inplace=True)


    ###################################################
    # Step 2 : Clean, Prepare and Manipulate Data
    ###################################################

    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate Data")
    print(Border)

    le_wether = LabelEncoder()
    le_temperature = LabelEncoder()
    le_play = LabelEncoder()

    Dataset["Wether"] = le_wether.fit_transform(
        Dataset["Wether"]
    )

    Dataset["Temperature"] = le_temperature.fit_transform(
        Dataset["Temperature"]
    )

    Dataset["Play"] = le_play.fit_transform(
        Dataset["Play"]
    )

    print("Data after Label Encoding :")
    print(Dataset)


    ###################################################
    # Features and Label
    ###################################################

    X = Dataset[["Wether", "Temperature"]]

    Y = Dataset["Play"]

    print(Border)
    print("Features are :")
    print(X)

    print(Border)
    print("Labels are :")
    print(Y)


    ###################################################
    # Step 3 : Train Data
    ###################################################

    print(Border)
    print("Step 3 : Train Data")
    print(Border)

    Model = KNeighborsClassifier(n_neighbors=3)

    Model.fit(X, Y)

    print("Model trained successfully")


    ###################################################
    # Step 4 : Test Data
    ###################################################

    print(Border)
    print("Step 4 : Test Data")
    print(Border)

    Wether = input(
        "Enter Wether (Sunny / Overcast / Rainy) : "
    )

    Temperature = input(
        "Enter Temperature (Hot / Mild / Cool) : "
    )

    WetherValue = le_wether.transform([Wether])[0]

    TemperatureValue = le_temperature.transform(
        [Temperature]
    )[0]

    TestData = pd.DataFrame(
        [[WetherValue, TemperatureValue]],
        columns=["Wether", "Temperature"]
    )

    Result = Model.predict(TestData)

    Answer = le_play.inverse_transform(Result)

    print(Border)
    print("Prediction is :", Answer[0])
    print(Border)


    ###################################################
    # Step 5 : Calculate Accuracy
    ###################################################

    CheckAccuracy(X, Y)


###################################################
# Starter
###################################################

if __name__ == "__main__":

    main()