def SumofDigit(no):
    sum = 0
    while no > 0:
        count = no % 10
        sum = sum + count
        no = no // 10
    return sum    

def main():
    no = int(input("Enter number : "))
    ret = SumofDigit(no)
    print(ret)

if __name__ =="__main__":
    main()