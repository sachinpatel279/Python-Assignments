def Binary(no):
    binary = bin(no)
    return binary[2:]

def main():
    no = int(input("Enter number : "))
    ret = Binary(no)
    print("Binary number : ",ret)

if __name__ == "__main__":
    main()