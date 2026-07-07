import Assignment17_1_Arithmetic
def Calculation(no1,no2):
    add = Assignment17_1_Arithmetic.Add(no1,no2)
    sub = Assignment17_1_Arithmetic.Sub(no1,no2)
    mul = Assignment17_1_Arithmetic.Mul(no1,no2)
    div = Assignment17_1_Arithmetic.Div(no1,no2)

    return add, sub, mul, div

def main():
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))   

    add, sub, mul, div = Calculation(no1, no2)
    print("Addition is:", add)
    print("Subtraction is:", sub)
    print("Multiplication is:", mul)
    print("Division is:", div)


if __name__ == "__main__":
    main()
