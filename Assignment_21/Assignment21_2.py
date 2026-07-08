import threading

def Maximum(Data):
    print("Maximum :", max(Data))


def Minimum(Data):
    print("Minimum :", min(Data))


def main():

    value = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements : ")
    
    for i in range(value):
        no = int(input())
        Data.append(no)

    t1 = threading.Thread(target=Maximum, args=(Data, ))
    t2 = threading.Thread(target=Minimum, args=(Data, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()