def CubeOfNumber(no1):
    return no1 * no1 * no1

def main():
    no1 = int(input("enter a number : "))
    CubeOfNumber(no1)
    ret = CubeOfNumber(no1)
    print("Cube : ",ret)

if __name__ == "__main__":
    main()