def factorial(a):
    fact = 1
    for i in range(1, a + 1):
        fact = fact * i
    return fact

def main():
    no = int(input("Enter a number: "))
    ret = factorial(no)
    print(f"Factorial is: {ret}")

if __name__== "__main__":
    main()
