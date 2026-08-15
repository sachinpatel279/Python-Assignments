import math

def MyEUCDistance(p1, p2):

    Ans = math.sqrt(
        (p1['StudyHours'] - p2['StudyHours']) ** 2 +
        (p1['Attendance'] - p2['Attendance']) ** 2
    )

    return Ans


def MyKNNClassifier():

    Border = "-" * 40

    Data = [
        {'StudyHours': 2, 'Attendance': 60, 'Result': 'Fail'},
        {'StudyHours': 5, 'Attendance': 80, 'Result': 'Pass'},
        {'StudyHours': 6, 'Attendance': 85, 'Result': 'Pass'},
        {'StudyHours': 1, 'Attendance': 50, 'Result': 'Fail'}
    ]

    print(Border)
    print("Student Result Prediction using KNN")
    print(Border)

    # Accept input from user
    StudyHours = int(input("Enter Study Hours: "))
    Attendance = int(input("Enter Attendance: "))

    NewStudent = {
        'StudyHours': StudyHours,
        'Attendance': Attendance
    }

    # Calculate Euclidean distance
    for d in Data:

        d['Distance'] = MyEUCDistance(
            d,
            NewStudent
        )

    # Sort according to distance
    SortedData = sorted(
        Data,
        key=lambda item: item['Distance']
    )

    # Select K nearest neighbours
    K = 3

    Nearest = SortedData[:K]

    print("\nNearest Neighbors:")

    for d in Nearest:
        print(
            "Study Hours:", d['StudyHours'],
            "Attendance:", d['Attendance'],
            "Result:", d['Result'],
            "Distance:", round(d['Distance'], 2)
        )

    # Majority Voting
    PassCount = 0
    FailCount = 0

    for d in Nearest:

        if d['Result'] == "Pass":
            PassCount = PassCount + 1

        elif d['Result'] == "Fail":
            FailCount = FailCount + 1

    if PassCount > FailCount:
        Prediction = "Pass"
    else:
        Prediction = "Fail"

    print(Border)
    print("Predicted Result:", Prediction)


def main():
    MyKNNClassifier()


if __name__ == "__main__":
    main()