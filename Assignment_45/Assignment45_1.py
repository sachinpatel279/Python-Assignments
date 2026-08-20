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

    print(df)

    return df

def main():
    df = CreateDataFrame()
    df = MathScrore(df)


if __name__ =="__main__":
    main()