import multiprocessing
import os

def Factorial(no):
    fact = 1 
    for i in range(1,no+1):
        fact = fact * i

    print(f"Process ID   : {os.getpid()}")
    print(f"Input Number : {no}")
    print(f"Factorial    : {fact}")
    print()

    return fact
    
def main():
    data = [10, 20, 30, 40]
    print(f"Input list : {data}")

    result = []
    p = multiprocessing.Pool()
    result = p.map(Factorial, data)
    p.close()
    p.join()

    print(result)

if __name__ == "__main__":
    main()