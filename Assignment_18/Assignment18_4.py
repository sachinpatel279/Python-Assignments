def Frequency(no, no1):
    count = 0
    for i in no:
        if i == no1:
            count += 1
    return count

def main():
    n = int(input("Enter a number: "))
    data = []
    for i in range(n):
        no = int(input("Enter elements : "))
        data.append(no)
    print("Input data is : ", data)
    no = int(input("Enter a number to search : "))
    ret =Frequency(data,no)
    print(f"Frequency of {no} is : {ret}")
if __name__ == "__main__":
    main()