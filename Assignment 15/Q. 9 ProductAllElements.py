from functools import reduce

product = lambda no1,no2 : no1 * no2

def main():
    data = [1,2,3,4,5]
    print("Input data is : ",data)
    rdata = reduce(product, data)
    print("data after reduce : ", rdata)

if __name__ == "__main__":
    main()