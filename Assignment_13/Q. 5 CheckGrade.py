def CheckGrade(marks):
    if marks>=75:
        return "Distinction"
    elif marks>=60 and marks<75:
        return "First Class"
    elif marks>=50 and marks<60:
        return "Second Class"
    else:
        return "Fail"

def main():
    marks = int(input("Enter number : "))
    ret = CheckGrade(marks)
    print("Grade : ",ret)

if __name__ == "__main__":
    main()