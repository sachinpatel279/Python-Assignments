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

    XValue = 6
    Y_predicted = m * XValue + c
    print("Predicted value of Y for X = ",XValue," is : ",Y_predicted)


def main():

    MySimpleLinearRegression()

if __name__ == "__main__":
    main()