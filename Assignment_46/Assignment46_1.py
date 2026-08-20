import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def MyLinearRegression(DataPath):

    Border = "-" * 50

    # Step 1 : Load the data
    print(Border)
    print("Step 1 : Load the data")
    print(Border)

    df = pd.read_csv(DataPath)

    print(df.head())

    # Step 2 : Clean, Prepare and Manipulate data
    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate data")
    print(Border)

    # Remove unwanted column
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print("\nData after removing unwanted columns:")
    print(df.head())

    # Check missing values
    print(Border)
    print("Checking Missing Values")
    print(Border)

    print(df.isnull().sum())

    # Remove missing records if any
    df = df.dropna()

    print("\nData after cleaning:")
    print(df.head())

    # Statistical Summary
    print(Border)
    print("Statistical Summary")
    print(Border)

    print(df.describe())

    # Correlation
    print(Border)
    print("Correlation")
    print(Border)

    print(df.corr())

    # Step 3 : Separate Independent and Dependent variables
    print(Border)
    print("Step 3 : Separate Independent and Dependent Variables")
    print(Border)

    X = df[["TV", "radio", "newspaper"]]
    Y = df["sales"]

    print("\nIndependent Variables:")
    print(X.head())

    print("\nDependent Variable:")
    print(Y.head())

    # Step 4 : Train and Test the data
    print(Border)
    print("Step 4 : Train and Test the Data")
    print(Border)

    # 50% Training and 50% Testing
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    print("Training Data :", X_train.shape)
    print("Testing Data  :", X_test.shape)

    # Create Linear Regression model
    print(Border)
    print("Creating Linear Regression Model")
    print(Border)

    model = LinearRegression()

    # Train the model
    model.fit(X_train, Y_train)

    print("Model Trained Successfully...")

    # Test the model
    print(Border)
    print("Testing the Model")
    print(Border)

    Y_pred = model.predict(X_test)

    # Step 5 : Display predicted and expected values
    print(Border)
    print("Step 5 : Predicted and Expected Values")
    print(Border)

    print("\nExpected Values:")
    print(Y_test.values)

    print("\nPredicted Values:")
    print(Y_pred)

    # Display first 10 values
    print(Border)
    print("First 10 Expected and Predicted Values")
    print(Border)

    Result = pd.DataFrame({
        "Expected Sales": Y_test.values,
        "Predicted Sales": Y_pred
    })

    print(Result.head(10))

    # Evaluate the model
    print(Border)
    print("Model Evaluation")
    print(Border)

    MAE = mean_absolute_error(Y_test, Y_pred)

    MSE = mean_squared_error(Y_test, Y_pred)

    RMSE = np.sqrt(MSE)

    R2 = r2_score(Y_test, Y_pred)

    print("MAE  :", MAE)
    print("MSE  :", MSE)
    print("RMSE :", RMSE)
    print("R2   :", R2)

    # Display Coefficients
    print(Border)
    print("Model Coefficients")
    print(Border)

    print("TV coefficient        :", model.coef_[0])
    print("Radio coefficient     :", model.coef_[1])
    print("Newspaper coefficient :", model.coef_[2])

    print("Intercept             :", model.intercept_)

    # Graph : Expected vs Predicted
    print(Border)
    print("Expected vs Predicted Graph")
    print(Border)

    plt.figure(figsize=(8, 5))

    plt.scatter(Y_test, Y_pred)

    plt.xlabel("Expected Sales")
    plt.ylabel("Predicted Sales")

    plt.title("Expected Sales vs Predicted Sales")
    plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color='red', linewidth=2)

    plt.show()


def main():

    MyLinearRegression("Advertising.csv")


if __name__ == "__main__":
    main()