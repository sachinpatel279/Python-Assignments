from sklearn.metrics import classification_report

def Classification_Report():

    Actual = [1, 1, 1, 1, 0, 0, 0, 0]
    Predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    Report = classification_report(Actual, Predicted)
    print("Classification Report : \n",Report)

def main():
    Classification_Report()

if __name__ == "__main__":
    main()