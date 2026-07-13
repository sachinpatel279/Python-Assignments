def PerfectNumber(no):
    sum = 0
    for i in range(1,no):
        if no % i == 0:
            sum = sum + i
    if sum == no:
        return "perfect number"
    else:
        return "not perfect number"

def main():
    no = int(input("Enter Number : "))
    ret = PerfectNumber(no)
    print(ret)

if __name__ == "__main__":
    main()