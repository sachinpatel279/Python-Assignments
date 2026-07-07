import MarvellousNum
def ListPrime(lst):
    sum = 0
    for i in lst:
            if MarvellousNum.ChkPrime(i):
                sum = sum + i
    return sum

def main():
    n = int(input("Enter a number: "))
    data = []
    print("Input Elements : ")
    for i in range(n):
        num = int(input())
        data.append(num)
    print(f"Input Elements : {data}")
    ret = ListPrime(data)
    print(f"Addition of Prime Numbers : {ret}")

if __name__== "__main__":
    main()