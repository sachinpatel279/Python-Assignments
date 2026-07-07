def SumList(data):
    sum = 0
    for i in data:
        sum = sum + i
    return sum

def main():
    n = int(input("Enter a number: "))
    data = []
    for i in range(n):
        no = int(input("Enter elements : "))
        data.append(no)
    print(f"Input data is : {data}")
    ret = SumList(data)
    print(f"Sum : {ret}")


if __name__ == "__main__":
    main()