###################################################
#   Importing required Libraries
###################################################

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score


Border = "-" * 40


###################################################
#   Step 1 : Get Data
###################################################

print(Border)
print("Step 1 : Get Data")
print(Border)

DataPath = "WinePredictor.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded Successfully")

print("\nInitial entries from Dataset are:")
print(df.head())

print("\nShape of Dataset:")
print(df.shape)


###################################################
#   Step 2 : Clean, Prepare and Manipulate Data
###################################################

print("\n" + Border)
print("Step 2 : Clean, Prepare and Manipulate Data")
print(Border)

print("\nMissing Values:")
print(df.isnull().sum())

# Input Features - 13 columns
X = df.drop("Class", axis=1)

# Output Label
Y = df["Class"]

print("\nFeatures are:")
print(X.head())

print("\nLabels are:")
print(Y.head())

print("\nAvailable Classes:")
print(Y.unique())


###################################################
#   Step 3 : Train Data
###################################################

print("\n" + Border)
print("Step 3 : Train Data")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

print("Training Data Size :", X_train.shape)
print("Testing Data Size  :", X_test.shape)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

print("Model Training Completed Successfully")


###################################################
#   Step 4 : Test Data
###################################################

print("\n" + Border)
print("Step 4 : Test Data")
print(Border)

Y_pred = model.predict(X_test)

print("\nActual Classes:")
print(Y_test.values)

print("\nPredicted Classes:")
print(Y_pred)


###################################################
#   Step 5 : Calculate Accuracy
###################################################

print("\n" + Border)
print("Step 5 : Calculate Accuracy")
print(Border)

Accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy :", Accuracy)

print("Accuracy Percentage :", Accuracy * 100, "%")