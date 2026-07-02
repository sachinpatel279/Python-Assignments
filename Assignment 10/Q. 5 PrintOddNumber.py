
def OddNumber(no):
    odd = list()
    for i in range(1,no+1,2):
        odd.append(i)
    return odd    

def main():
    no = int(input("Enter number : "))
    ret = OddNumber(no)
    print(*ret)


if __name__ == "__main__":
    main()