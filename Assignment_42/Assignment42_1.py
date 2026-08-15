import math

def MarvellousEUCDistance(p1, p2):

    Ans = math.sqrt(
        (p1['X'] - p2['X']) ** 2 +
        (p1['Y'] - p2['Y']) ** 2
    )

    return Ans

def MarvellousKNNClassifier():

    Border = "-" * 40

    Data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'}
    ]

    print(Border)
    print("Marvellous KNN Classifier")
    print(Border)

    X = int(input("Enter X coordinate: "))
    Y = int(input("Enter Y coordinate: "))

    NewPoint = {'X': X, 'Y': Y}

    # Calculate Euclidean distance
    for d in Data:
        d['distance'] = MarvellousEUCDistance(d, NewPoint)

    # Sort according to distance
    SortedData = sorted(
        Data,
        key=lambda item: item['distance']
    )

    # Select K nearest neighbours
    K = 3

    Nearest = SortedData[:K]

    print("\nNearest Neighbors:")

    for d in Nearest:
        print(
            d['point'],
            "- Distance:",
            round(d['distance'], 2)
        )

    # Majority Voting

    RedCount = 0
    BlueCount = 0

    for d in Nearest:

        if d['label'] == "Red":
            RedCount = RedCount + 1

        elif d['label'] == "Blue":
            BlueCount = BlueCount + 1

    if RedCount > BlueCount:
        Prediction = "Red"
    else:
        Prediction = "Blue"

    print("\nPredicted Class:", Prediction)


def main():
    MarvellousKNNClassifier()


if __name__ == "__main__":
    main()