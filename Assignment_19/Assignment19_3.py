Check = lambda no: no >= 70 and no <= 90

Increase = lambda no: no + 10

Product = lambda no1, no2: no1 * no2


def filterX(Task, Elements):
    Result = []

    for no in Elements:
        if Task(no):
            Result.append(no)

    return Result


def mapX(Task, Elements):
    Result = []

    for no in Elements:
        Result.append(Task(no))

    return Result


def reduceX(Task, Elements):
    product = 1

    for no in Elements:
        product = Task(product, no)

    return product


def main():

    size = int(input("Enter number of elements : "))

    Data = []

    print("Enter elements :")

    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input List :", Data)

    FData = filterX(Check, Data)
    print("List after Filter :", FData)

    MData = mapX(Increase, FData)
    print("List after Map :", MData)

    RData = reduceX(Product, MData)
    print("Output of Reduce :", RData)


if __name__ == "__main__":
    main()