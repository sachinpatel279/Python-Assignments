import threading

def checkPrime(no):
    if no < 2:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True

def Prime(Data):
    PrimeList = []
    for no in Data:
        if checkPrime(no) == True:
            PrimeList.append(no)
    print("Prime Numbers : ", PrimeList)
    
def NonPrime(Data):
    NonPrimeList = []
    for no in Data:
        if checkPrime(no) == False:
            NonPrimeList.append(no)
    print("NonPrime Numbers : ", NonPrimeList)
    
def main():
    Data = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print("Input List : ", Data)

    t1 = threading.Thread(target=Prime,    args=(Data, ))
    t2 = threading.Thread(target=NonPrime, args=(Data, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()