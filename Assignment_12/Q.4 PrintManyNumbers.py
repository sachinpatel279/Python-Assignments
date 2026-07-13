def Number(no):
    num = list()
    for i in range(1,no+1):
        num.append(i)
    return num

def main():
    no = int(input("Enter number :"))
    ret = Number(no)
    print(*ret)

if __name__ == "__main__":
    main()