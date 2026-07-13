def SumOfNaturalNo(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum + i
    return sum    


def main():
    no = int(input("Enter a number : "))
    ret = SumOfNaturalNo(no)
    print("Sum is : ",ret)


if __name__ == "__main__":
    main()