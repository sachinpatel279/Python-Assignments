import numpy as np
from sklearn.preprocessing import StandardScaler

def ScaledDataSet():

    Data = np.array([[25, 20000],
                     [30, 40000],
                     [35, 80000]])

    Scaler = StandardScaler()
    ScaledData = Scaler.fit_transform(Data)

    print("Original Data : \n",Data)
    print("Scaled Data : \n",ScaledData)

def main():
    ScaledDataSet()

if __name__ == "__main__":
    main()
    