import threading

def EvenFactor(no):
    print("Even Factors : ")
    sum = 0
    for i in range(2,no+1,2):
        if no % i == 0:
            print(i, end= " ")
            sum = sum + i
    print("\nSum of Even Factors : ", sum )

def OddFactor(no):
    print("Odd Factors : ")
    sum = 0 
    for i in range(1,no+1,2):
        if no % i == 0 :
            print(i,end=" ")
            sum =sum + i
    print("\nSum of Odd Factors : ", sum)




def main():
    no = int(input("Enter number : "))
    t1= threading.Thread(target=EvenFactor,args=(no, ))
    t2= threading.Thread(target=OddFactor,args=(no, ))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ =="__main__":
    main()