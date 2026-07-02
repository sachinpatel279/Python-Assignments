divisible = lambda no: True if no % 5 == 0 else False   

def main():
    no = int(input("Enter a number: "))
    ret = divisible(no)
    print(ret)

if __name__== "__main__":
    main()