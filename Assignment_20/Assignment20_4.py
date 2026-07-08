import threading
def Small(value):
    count = 0
    for ch in value:
        if ch.islower():
            count=count + 1
    
    print(f"Thread ID : {threading.get_ident()}")
    print(f"Thread Name : {threading.current_thread().name}")
    print(f"Small characters : {count}")

def Capital(value):
    count = 0
    for ch in value:
        if ch.isupper():
            count=count + 1
    
    print(f"Thread ID : {threading.get_ident()}")
    print(f"Thread Name : {threading.current_thread().name}")
    print(f"Upper characters : {count}")


def Digits(value):
    count = 0
    for ch in value:
        if ch.isdigit():
            count=count + 1
    
    print(f"Thread ID : {threading.get_ident()}")
    print(f"Thread Name : {threading.current_thread().name}")
    print(f"Digits : {count}")


def main():
    value =input("Enter a string : ")
    t1=threading.Thread(target=Small, args=(value, ))
    t2=threading.Thread(target=Capital, args=(value, ))
    t3=threading.Thread(target=Digits,args=(value, ))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t2.join()

if __name__ =="__main__":
    main()