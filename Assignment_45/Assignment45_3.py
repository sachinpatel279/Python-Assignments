import pandas as pd

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

def main():
    df = CreateDataFrame()
    df = MathScrore(df)
    df = AddGenderColumn(df)
    df = CalculateAverage(df)


if __name__ =="__main__":
    main()