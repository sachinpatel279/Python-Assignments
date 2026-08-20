
def CalculateValues():

    Actual = [1, 1, 1, 1, 0, 0, 0, 0]
    Predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for i in range(len(Actual)):
        if Actual[i] == 1 and Predicted[i] == 1:
            TP  = TP + 1
        elif Actual[i] == 0 and Predicted[i] == 0:
            TN = TN + 1
        elif Actual[i] == 0 and Predicted[i] == 1:
            FP = FP + 1
        elif Actual[i] == 1 and Predicted[i] == 0:
            FN = FN + 1

    print("True Positive : ",TP)
    print("True Negative : ",TN)
    print("False Positive : ",FP)
    print("False Negative : ",FN)

def main():
    CalculateValues()

if __name__ == "__main__":
    main()