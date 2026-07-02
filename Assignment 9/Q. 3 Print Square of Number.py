def SquareNumber(no1):
    return no1 * no1

def main():
    no1 =int(input("Enter a number : "))
    ret = SquareNumber(no1)
    print("Square of number is : ",ret)

if __name__ == "__main__":
    main()