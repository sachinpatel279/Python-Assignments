def MinNumber(no):
    min = no[0]
    for i in no:
        if i < min:
            min = i
    return min


def main():
    n = int(input("Enter a number: "))
    data = []
    for i in range(n):
        no = int(input("Enter elements : "))
        data.append(no)
    print(f"Input data is : {data}")
    ret = MinNumber(data)
    print(f"Min is : {ret}")

if __name__ == "__main__":
    main()