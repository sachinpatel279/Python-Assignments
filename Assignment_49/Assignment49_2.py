
import numpy as np

def CalVarienceAndSD():

    Data = np.array([6,7,8,9,10,11,12])

    Varience = np.var(Data)
    Standard_Deviation = np.std(Data)  

    print("Varience of Data : ",Varience)
    print("Standard Deviation of Data : ",Standard_Deviation)

def main():
    CalVarienceAndSD()

if __name__ == "__main__":
    main()