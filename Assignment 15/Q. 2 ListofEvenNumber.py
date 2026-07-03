Evenlist = lambda no : no % 2 == 0

def main():
    data = [1,2,3,4,5,6,7,8]
    print("Input data is : ",data)
    fdata =list(filter(Evenlist, data))
    print("data after filter : ", fdata)

if __name__ == "__main__":
    main()
