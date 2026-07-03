
divisible = lambda no : no % 3 == 0 and no % 5 == 0

def main():
    data = [15,10,30,7,45,6]
    print("Input data is : ",data)
    fdata = list(filter(divisible, data))
    print("data after filter : ", fdata)
    
if __name__ == "__main__":
    main()