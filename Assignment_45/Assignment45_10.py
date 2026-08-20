import pandas as pd
import matplotlib.pyplot as plt

def CreateDataFrame():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)
    return df

def MathScrore(df):
    Min = df["Math"].min()
    Max = df["Math"].max()

    df["Math"] = (df["Math"] - Min) / (Max - Min)
    print("\n Dataframe after normalization of Math score is : ")
    print(df)

    return df

def AddGenderColumn(df):
    df["Gender"] = ["Male", "Male", "Female"]

    df = pd.get_dummies(df, columns=["Gender"], dtype=int)
    print("\n Dataframe after adding Gender column")

    print(df)
    return df

def CalculateAverage(df):
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82],
        'Gender': ['Male', 'Male', 'Female']
    }

    df = pd.DataFrame(data)

    df["Total"] = (df["Math"] + df["Science"] + df["English"])

    Result = df.groupby("Gender")[["Math", "Science", "English", "Total"]].mean()
    print("\n Average score of Male and Female students is : ")
    print(Result)

    return df

def SagarPieChart(df):

    Sagar = df[df["Name"] == "Sagar"].iloc[0]

    Subjects = ["Math", "Science", "English"]
    Marks = [Sagar["Math"], Sagar["Science"], Sagar["English"]]

    plt.figure(figsize=(6, 6))
    plt.pie(Marks, labels=Subjects, autopct="%1.1f%%")
    plt.title(" Sagar Subject Marks  : ")
    plt.show()

    return df

def AddStatus(df):

    df["Status"] = df["Total"].apply(lambda x: "Pass" if x >= 250 else "Fail")
    print("\n Dataframe after adding Status column")
    print(df)

    return df

def CountStudentsPassed(df):
    PassedCount = df[df["Status"] == "Pass"].shape[0]
    print("\n Count of students who passed : ", PassedCount)

    return df

def ExportToCSV(df, filename):
    df.to_csv(filename, index=False)
    print(f"\n Dataframe exported to {filename} successfully.")

    return df

def HistrogramOfMath(df):
    plt.figure(figsize=(6, 5))
    plt.hist(df["Math"], bins=10, color='blue', edgecolor='black')
    plt.title("Histogram of Math Scores")
    plt.xlabel("Math Scores")
    plt.ylabel("Number of Students")
    plt.show()

    return df

def RenameMathColumn(df):
    df.rename(columns={"Math": "Mathematics"}, inplace=True)
    print("\n Dataframe after renaming Math column to Mathematics : ")
    print(df)

    return df

def BoxPlotOfEnglish(df):
    plt.figure(figsize=(6, 5))
    plt.boxplot(df["English"])
    plt.title("Box Plot of English Marks")
    plt.ylabel("English Marks")
    plt.show()

    return df

def main():
    df = CreateDataFrame()
    df = MathScrore(df)
    df = AddGenderColumn(df)
    df = CalculateAverage(df)
    df = SagarPieChart(df)
    df = AddStatus(df)
    df = CountStudentsPassed(df)
    df = ExportToCSV(df, "Final_Student_Data.CSV")
    df = HistrogramOfMath(df)
    df = RenameMathColumn(df)
    BoxPlotOfEnglish(df)    

if __name__ =="__main__":
    main()