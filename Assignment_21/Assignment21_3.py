import threading

Counter = 0
Lock = threading.Lock()

def Increment():

    global Counter
    for i in range(10):
        Lock.acquire()
        Counter = Counter + 1
        Lock.release()

def main():

    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final Counter :", Counter)

if __name__ == "__main__":
    main()