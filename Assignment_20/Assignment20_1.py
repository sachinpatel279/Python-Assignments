import threading

def Even():
    print("Even numbers : ")
    for i in range(2,21,2):
        print(i,end=" ")
    print()    

def Odd():
    print("Odd numbers : ")
    for i in range(1,20,2):
        print(i,end=" ")
    print()

def main():
    t1= threading.Thread(target= Even,  name="Even")
    t2= threading.Thread(target= Odd, name="Odd")
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()