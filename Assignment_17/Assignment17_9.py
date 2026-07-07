def countDigit(a):
    cnt = 0
    while a > 0:
        cnt += 1
        a = a // 10
    return cnt 

def main():
    no = int(input("Enter a number: "))
    ret = countDigit(no)
    print(ret)


if __name__ == "__main__":
    main()
