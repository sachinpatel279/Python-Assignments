
from functools import reduce

min = lambda a,b : a if a < b else b

def main():
    data = [3,7,1,9,2,4]
    print("Input data is : ",data)
    rdata = reduce(min, data)
    print("Minimum element is : ",rdata)
if __name__ == "__main__":
    main()