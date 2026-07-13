
from functools import reduce

Addition = lambda x,y : x + y

def main():
    data = [1,2,3,4,5]
    print("Input data is : ",data)
    rdata = reduce(Addition, data)  
    sum = rdata    
    print("data after reduce : ",sum)
    
if __name__ == "__main__":
    main()