import pandas as pd
from sklearn.linear_model import LinearRegression

def main():
    # Create a dataset
    data = {
        "StudyHours": [1, 2, 3, 4, 5],
        "Marks": [50, 55, 60, 65, 70]
    }

    df = pd.DataFrame(data)

    # Prepare the data for linear regression
    X = df[["StudyHours"]]
    y = df["Marks"]

    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    StudyHours =[[6]]
    PredictedMarks = model.predict(StudyHours)
    print(f"Predicted Marks for {StudyHours[0][0]} study hours: {PredictedMarks[0]}")

    print("Coefficient :", model.coef_[0])
    print("Intercept   :", model.intercept_)

if __name__ == "__main__":
    main()