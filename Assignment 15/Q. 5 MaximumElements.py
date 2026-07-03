
from functools import reduce

max = lambda x,y : x if (x > y) else y


def main():
    data = [3,1,7,2,9,4]
    print("Input data is : ",data)
    rdata = reduce(max, data)
    print("Maximum element is : ",rdata)
if __name__ == "__main__":
    main()