def ChkNum(no):
    if no % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

def main():
    no = int(input("Enter a number: "))
    ret = ChkNum(no)
    print(ret)
if __name__== "__main__":
    main()
