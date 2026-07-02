def EvenNumber(no):
    even = list()
    for i in range(1,no+1):
        if i % 2 == 0:
            even.append(i)
    return even    


def main():
    no = int(input("Enter number : "))
    ret = EvenNumber(no)
    print(*ret)

if __name__ == "__main__":
    main()    