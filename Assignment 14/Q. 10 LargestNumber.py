largest = lambda no1,no2,no3: no1 if no1 > no2 and no1 > no3 else(no2 if no2 > no3 else no3)

def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    no3 = int(input("Enter third number: "))
    ret = largest(no1, no2, no3)
    print("Largest number is : ", ret)

if __name__== "__main__":
    main()