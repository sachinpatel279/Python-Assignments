
def pattern(a):
    for i in range(a):
        for j in range(a):
            print("*", end=" ")
        print()
def main():
    no = int(input("Enter a number: "))
    pattern(no)

if __name__ == "__main__":
    main()
