def CheckPrime(no):
    if no < 2:
        return False
    for i in range(2,no):
        if no % i == 0:
            return False
    return True

MultiplyTwo = lambda no: no * 2 

MaxNumber = lambda no1, no2 : no1 if no1 > no2 else no2

def FilterX(Task, Elements):
    Result = []
    for no in Elements:
        ret = Task(no)
        if(ret == True):
            Result.append(no)
    return Result

def MapX(Task, Elements):
    Result = []
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result

def ReduceX(Task, Elements):
    sum = 0
    for no in Elements:
        sum = Task(sum, no)
    return sum


def main():
    size = int(input("Enter number of elements : "))
    Data = []
    print("Input Elements : ")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input List : ", Data)
    FData = list(FilterX(CheckPrime, Data))
    print("Data After Filter : ", FData)

    MData = list(MapX(MultiplyTwo, FData))
    print("Data After Map : ", MData)

    RData = ReduceX(MaxNumber, MData)
    print('Data After Reduce : ', RData)

if __name__ == "__main__":
    main()