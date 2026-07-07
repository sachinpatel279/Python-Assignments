def MaxNumber(no):
    max = no[0]
    for i in no:
        if i > max:
            max = i
    return max


def main():
    n = int(input("Enter a number: "))
    data = []
    for i in range(n):
        no = int(input("Enter elements : "))
        data.append(no)
    print(f"Input data is : {data}")
    ret = MaxNumber(data)
    print(f"Max is : {ret}")

if __name__ == "__main__":
    main()