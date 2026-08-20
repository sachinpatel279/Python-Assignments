import numpy as np

def CalculateMean():

    data = np.array([6,7,8,9,10,11,12])

    Mean = np.mean(data)

    print("Mean of Data : ",Mean)

def main():
    CalculateMean()

if __name__ == "__main__":
    main() 
    