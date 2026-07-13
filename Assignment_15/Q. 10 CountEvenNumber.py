
CheckEven = lambda no : (no % 2 == 0) 

def main():
    data = [1,2,3,4,5,6,7,8]
    print("Input data is : ",data)

    fdata = list(filter(CheckEven, data))
    count = len(fdata)
    print("data after filter : ",count)

if __name__ == "__main__":
    main()