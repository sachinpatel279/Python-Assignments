

def evenNumber(a):
    for i in range(2, a+1, 2):
        print(i, end=" ")
def main():
    no = int(input("Enter a number: "))
    evenNumber(no)

if __name__== "__main__":
    main()
