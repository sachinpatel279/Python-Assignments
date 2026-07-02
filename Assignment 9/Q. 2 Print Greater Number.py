def ChkGreater(no1, no2):
    if no1 > no2 :
        return no1
    else :
        return no2

def main():
    no1 =int(input("Enter first number : "))
    no2 =int(input("Enter second number : "))

    ret = ChkGreater(no1, no2)
    print("Greater Number is : ", ret)

if __name__ == "__main__":
    main()    