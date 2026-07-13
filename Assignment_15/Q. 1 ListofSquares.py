SquareList = lambda no : no * no

def main():
    data = [1,2,3,4,5]
    print("Input data is : ",data)
    mdata = list(map(SquareList, data))
    print("data after map : ",mdata)

if __name__ == "__main__":
    main()