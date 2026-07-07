def pattern(a):
    for i in range(a):
        for j in range(a):
            if j + i <=4: 
             print("*", end=" ")
        print()

def main():
    no = int(input("Enter a number: "))
    pattern(no)

if __name__ == "__main__":
    main()
