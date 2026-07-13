Cube = lambda no: no * no * no

def main():
    no = int(input("Enter a number: "))
    ret = Cube(no)
    print("Cube of number is : ", ret)

if __name__== "__main__":
    main()