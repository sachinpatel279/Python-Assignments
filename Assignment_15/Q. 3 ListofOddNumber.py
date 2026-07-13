
CheckOdd = lambda no : no % 2 != 0

def main():
    data = [1,2,3,4,5,6,7,8]
    print("Inout data is : ",data)
    fdata = list(filter (CheckOdd, data))
    print("data after filter : ", fdata)
if __name__ == "__main__":
    main()