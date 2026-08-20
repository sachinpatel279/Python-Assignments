import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
def MySimpleLinearRegression():

    Experience = [1,2,3,4,5]
    Salary = [20000,25000,30000,35000,40000]

    X = np.array(Experience).reshape(-1,1)
    Y = np.array(Salary)

    model = LinearRegression()

    model.fit(X, Y)

    print("Coefficent = ", model.coef_[0])
    print("Y intercept (c) = ", model.intercept_)

    new_experience = 6
    predicted_salary = model.predict([[new_experience]])

    print("Predicted salary for experience :  ",predicted_salary[0])

    Y_pred = model.predict(X)

    plt.scatter(Experience, 
                Y_pred,
                label = "Regression points",
                )

    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Experience VS Salary")
    plt.plot(Experience, Y_pred, color = 'red', label = "Regression Line")
    plt.legend()
    plt.show()
    

def main():

    MySimpleLinearRegression()

if __name__ == "__main__":
    main()