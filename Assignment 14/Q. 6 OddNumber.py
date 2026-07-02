odd = lambda no: True if no % 2 !=0 else False

def main():
    no = int(input("Enter a number: "))
    ret = odd(no)
    print(ret)
if __name__== "__main__":
    main()