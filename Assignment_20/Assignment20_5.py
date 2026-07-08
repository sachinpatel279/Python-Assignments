import threading

def Display1():
    print("Thread 1: -----1 to 50-----------")
    for i in range(1, 51):
        print(i, end=" ")
    print()


def Display2():
    print("Thread 2 : -------50 to 1---------")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()


def main():

    t1 = threading.Thread(target=Display1)
    t2 = threading.Thread(target=Display2)

    t1.start()
    t1.join()     

    t2.start()
    t2.join()      

if __name__ == "__main__":
    main()