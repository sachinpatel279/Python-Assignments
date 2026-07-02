def AreaOfRect(length, width):
    area = length * width
    return area


def main():
    length = int(input("Enter length : "))
    width = int(input("Enter width : "))
    ret = AreaOfRect(length, width)
    print("Area of Rectangle : ", ret)

if __name__ == "__main__":
    main()