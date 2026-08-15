import pandas as pd

Border = "-"*30
##############################
#   Step 1:Load the dataset
##############################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)      #df means DataFrame (2d array)

print("Dataset loaded Successfully")
print("Inital entries from Dataset are:")
print(df.head())
print(df.tail())

print("Shape of dataset :",df.shape)

print("Column names :",list(df.columns))

print(df.dtypes)
