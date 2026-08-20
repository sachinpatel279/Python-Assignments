import pandas as pd
import matplotlib.pyplot as plt

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


def main():
    df = Create_DataFrame()
    DisplayInfo(df)
    AddTotal(df)
    DisplayStudents(df)
    ReplaceName(df)
    SortByDecendingOrder(df)
    PlotTotalMarks(df)



if __name__ == "__main__":
    main()