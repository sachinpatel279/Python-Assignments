import multiprocessing
import time

def PowerFive(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum + i**5
    
    return sum

def main():

    data = [10000, 20000, 30000, 40000, 5000, 6000, 7000, 8000]
    print(f"Input list : {data}")

    start_time = time.perf_counter()

    result = []
    p = multiprocessing.Pool()
    result = p.map(PowerFive, data)

    end_time = time.perf_counter()
    
    print(f"Result : {result}")
    print(f"Time Required is : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()