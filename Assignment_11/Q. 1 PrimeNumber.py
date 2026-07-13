def PrimeNumber(no):
    for i in range(2,no):
        if no % i == 1:
            return "prime number"
        else:
            return "not prime number"


def main():
    no = int(input("Enter number : "))
    ret = PrimeNumber(no)
    print(ret)

if __name__ == "__main__":
    main()