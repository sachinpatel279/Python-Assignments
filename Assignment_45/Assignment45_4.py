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


def main():
    df = CreateDataFrame()
    df = MathScrore(df)
    df = AddGenderColumn(df)
    df = CalculateAverage(df)
    df = SagarPieChart(df)


if __name__ =="__main__":
    main()