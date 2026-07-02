
def reverse(no):
    num = list()
    for i in range(no,0,-1):
        num.append(i)
    return num

def main():
    no = int(input("Enter number : "))
    ret = reverse(no)
    print(*ret)

if __name__ == "__main__":
    main()