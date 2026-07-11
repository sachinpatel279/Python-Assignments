import multiprocessing

def SumOdd(no):
    sum = 0 
    for i in range(1,no+1,2):
        sum = sum + i

    return sum

def main():
    data = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
    print(f"Input list : {data}")

    result = []
    p = multiprocessing.Pool()
    result = p.map(SumOdd, data)
    p.close()
    p.join()
    
    print(result)

if __name__ == "__main__":
    main()