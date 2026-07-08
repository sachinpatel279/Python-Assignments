import threading

def EvenList(data):
    even= []
    for no in data:
        if no % 2 == 0:
            even.append(no)
    print(f"Even List : {even}")
    print(f"Sum of Even : {sum(even)}")

def OddList(data):
    odd = []
    for no in data:
        if no % 2 != 0:
            odd.append(no)
    print(f"Odd List : {odd}")
    print(f"Sum of Odd :{sum(odd)}")

def main():
    data = [1,2,3,4,5,6,7,8,9,10]
    t1= threading.Thread(target=EvenList,args=(data, ))
    t2=threading.Thread(target=OddList,args=(data, ))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()