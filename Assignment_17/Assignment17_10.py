
def SumOfDigit(no):
    sum = 0
    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10
    return sum


def main():
    no = int(input("Enter a number: "))
    ret = SumOfDigit(no)
    print(ret)


if __name__ == "__main__":
    main()
