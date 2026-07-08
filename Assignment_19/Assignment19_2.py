multi = lambda no1,no2 : no1*no2


def main():
    no1 = int(input("enter first number : "))
    no2 = int(input("enter second number : "))
    ret =multi(no1,no2)
    print(f"multiplication is : {ret}")

if __name__ =="__main__":
    main()