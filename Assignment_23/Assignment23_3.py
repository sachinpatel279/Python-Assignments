import multiprocessing

def CheckPrime(no):

    if no < 2:
       return False
    for i in range(2,int(no ** 0.5)+1):
        if no % i == 0:
            return False
    return True

def CountPrime(no):
    count = 0
    for i in range(1,no+1):
        if CheckPrime(i) == True:
            count = count+1
    return count

def main():
    data = [10000, 20000, 30000, 40000, 5000, 6000, 7000, 8000]
    print(f"Input list : {data}")

    p=multiprocessing.Pool()
    result = []
    result = p.map(CountPrime, data)
    p.close()
    p.join()
    print(result)

if __name__ == "__main__":
    main()