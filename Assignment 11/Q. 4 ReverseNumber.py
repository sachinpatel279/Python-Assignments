def ReverseNumber(no):
    rev = 0
    while no > 0:
        num = no % 10
        rev = rev * 10 + num
        no = no // 10
    return rev


def main():
    no = int(input("Enter number : "))
    ret = ReverseNumber(no)
    print(ret)

if __name__ == "__main__":    
    main()