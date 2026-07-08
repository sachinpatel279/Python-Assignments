CheckEven = lambda no: no % 2 == 0
Square = lambda no: no * no
Addition = lambda no1, no2: no1 + no2

def filterX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no) 
        if(Ret == True):
            Result.append(no)  
    return Result

def mapX(Task, Elements):
    Result = []
    for no in Elements:
        Result.append(Task(no))
    return Result

def reduceX(Task, Elements):
    sum = 0
    for no in Elements:
        sum = Task(sum, no)
    return sum


def main():
    size = int(input("Enter number of elements : "))
    Data = []
    print("Enter elements :")

    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input List :", Data)

    FData = filterX(CheckEven, Data)
    print("List after Filter :", FData)

    MData = mapX(Square, FData)
    print("List after Map :", MData)

    RData = reduceX(Addition, MData)
    print("Output of Reduce :", RData)

if __name__ == "__main__":
    main()