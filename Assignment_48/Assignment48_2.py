def MySimpleLinearRegression():

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    mean_x = sum_x / len(X)
    mean_y = sum_y / len(Y)
    print("Mean of X = ",mean_x)
    print("Mean of Y = ",mean_y)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator
    print("Slope (m) = ",m)

    c = mean_y - m * mean_x
    print("Y intercept (c) = ",c)

    print(" Regression Equation: Y = ",m,"X + ",c)

    Predicted_Y = []

    print("Acutal Y     Predicted Y     Error                           Error Squared")
    Sum_Error_Squared = 0

    for i in range(n):
        Prediction = m * X[i] + c
        Predicted_Y.append(m * X[i] + c)

        Error = Y[i] - Prediction
        Error_Squared = Error ** 2

        Sum_Error_Squared = Sum_Error_Squared + Error_Squared

        print(Y[i],"          ",Prediction,"          ",Error,"          ",Error_Squared)

        MSE = Sum_Error_Squared / n

        SST = 0

        for value in Y:
            SST = SST + (value - mean_y) ** 2

        R2 = 1 - (Sum_Error_Squared / SST)  

    print("R-squared (R2) = ",R2)

    print("Mean Squared Error (MSE) = ",MSE)



def main():

    MySimpleLinearRegression()

if __name__ == "__main__":
    main()