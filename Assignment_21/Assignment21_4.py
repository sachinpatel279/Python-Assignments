import threading
def computeSum(Data):
    sum = 0
    for no in Data:
        sum = sum + no
    print("Sum of elements : ", sum)
def computeProduct(Data):
    product = 1
    for no in Data:
        product = product * no
    print("Product of elements: ", product)

def main():
    no = int(input("Number of elements : "))
    Data = []
    print("Enter Elements : ")
    for i in range(no):
        no = int(input())
        Data.append(no)
    print("Input List : ", Data)
    t1 = threading.Thread(target=computeSum, args=(Data, ))
    t2 = threading.Thread(target=computeProduct, args=(Data, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
if __name__ == "__main__":
    main()