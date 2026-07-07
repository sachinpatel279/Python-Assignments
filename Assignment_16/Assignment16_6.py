def PositiveNegative(no):
    if no < 0:
        return "Negative Number"
    elif no > 0:
        return "Positive Number"
    else:
        return "Zero"

def main():
    a = int(input("Enter a number: "))
    ret = PositiveNegative(a)
    print(ret)    

if __name__== "__main__":
    main()
