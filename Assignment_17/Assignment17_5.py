def PrimeNumber(value):
    if value <= 1:
        return f"{value} is not a prime number"

    for i in range(2, value):
        if value % i == 0:
            return f"{value} is not a prime number"

    return f"{value} is a prime number"

def main():
    no = int(input("Enter a number: "))
    ret = PrimeNumber(no)
    print(ret)


if __name__ == "__main__":
    main()