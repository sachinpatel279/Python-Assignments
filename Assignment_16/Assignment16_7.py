def DivisibleByFive(a):
    if a % 5 == 0:
        return True
    else:
        return False
    
def main():
    no = int(input("Enter a number: "))
    ret = DivisibleByFive(no)
    print(ret)
if __name__== "__main__":
    main()