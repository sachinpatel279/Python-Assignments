add = lambda no1, no2 : no1 + no2

def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    ret = add(no1, no2)
    print("Addition of two numbers is : ", ret)

if __name__ == "__main__":
    main()