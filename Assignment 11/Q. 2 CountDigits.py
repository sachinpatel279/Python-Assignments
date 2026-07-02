
def CountDigit(no):
    count = 0
    while no > 0:
        no = no//10
        count=count + 1
    return count

def main():
    no = int(input("Enter number : "))
    ret = CountDigit(no)
    print(ret)

if __name__ =="__main__":
    main()    