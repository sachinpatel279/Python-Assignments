def AreaOfCircle(radius):
    area = 3.14 * radius * radius
    return area

def main():
    radius = int(input("Enter radius : "))
    ret =AreaOfCircle(radius)
    print("Area of circle : ",ret)

if __name__ == "__main__":
    main()