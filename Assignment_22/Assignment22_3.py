import multiprocessing

def CountEven(no):
    count = 0 
    for i in range(2,no+1,2):
        count = count + 1

    return count
    
def main():
    data = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
    print(f"Input list : {data}")

    result = []
    p = multiprocessing.Pool()
    result = p.map(CountEven, data)
    p.close()
    p.join()
    print(result)

if __name__ == "__main__":
    main()