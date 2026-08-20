import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Create_DataFrame():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)
    return df

def DisplayInfo(df):
    print("Shape : ",df.shape)
    print("Columns : ",df.columns)
    print("Data type :\n",df.dtypes)
    print("Descriptive Statistics : \n",df.describe())

def AddTotal(df):
    df["Total"] = df["Math"] + df["Science"] + df["English"]

    print("\nDataframe after adding total : ")
    print(df)

def DisplayStudents(df):

    Result = df[df["Science"] > 85]
    print("\nStudents name who score more than 85 marks  in science : ")
    print(Result)

def ReplaceName(df):

    df["Name"] = df["Name"].replace("Pooja","Puja")
    print("\nDataframe after replacing Pooja name with Puja")
    print(df)

def SortByDecendingOrder(df):
    df =df.sort_values(by="Total", ascending = False)
    print("\nDataframe sorted by total marks in descending order : ")
    print(df)

def PlotTotalMarks(df):

    plt.bar(df["Name"], df["Total"])
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.title("Student Name vs Total Marks")
    plt.show()

def PlotAmitMarks(df):

    Amit = df[df["Name"]  == "Amit"]
    Subjects = ["Math", "Science", "English"]

    Marks = [
        Amit["Math"].values[0],
        Amit["Science"].values[0],
        Amit["English"].values[0]
        ]

    plt.plot(Subjects,Marks,marker = "o")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit marks across all subjects")
    plt.grid()
    plt.show()

def HandleMissingValues(df):
    data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
    }

    df2 = pd.DataFrame(data2)
    print("\n Dataframe before filling missing values from data2 ")
    print(df2)

    df2["Math"] = df2["Math"].fillna(df2["Science"].mean())
    df2["Science"] = df2["Science"].fillna(df2["Science"].mean())

    print("\n Dataframe after filling missing values from data2 ")
    print(df2)


def main():
    df = Create_DataFrame()
    DisplayInfo(df)
    AddTotal(df)
    DisplayStudents(df)
    ReplaceName(df)
    SortByDecendingOrder(df)
    PlotTotalMarks(df)
    PlotAmitMarks(df)
    HandleMissingValues(df)



if __name__ == "__main__":
    main()