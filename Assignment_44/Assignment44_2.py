import pandas as pd

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
    print("Data type : \n",df.dtypes)
    print("Descriptive Statistics : \n",df.describe())


def main():
    df = Create_DataFrame()
    DisplayInfo(df)

if __name__ == "__main__":
    main()