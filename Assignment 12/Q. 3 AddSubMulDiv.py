def calculation(no1,no2):
    add = no1 + no2
    sub = no1 - no2
    mul = no1 * no2
    div = no1 / no2
    return add, sub, mul, div

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    add,sub,mul,div = calculation(no1,no2)
    
    print("Addition is : ", add)
    print("Substraction is : ", sub)
    print("Multiplication is : ", mul)
    print("Division is : ", div)

    

if __name__ == "__main__":
    main()