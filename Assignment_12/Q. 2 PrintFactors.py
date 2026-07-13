def factors(no):
    fact = list()
    for i in range(1, no+1):
        if no % i == 0:
            fact.append(i)
    return fact        

def main():
    no = int(input("Enter number :"))
    ret = factors(no)
    print(*ret)

if __name__ == "__main__":
    main()