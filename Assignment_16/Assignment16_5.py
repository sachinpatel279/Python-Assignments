def reverse(a):
    for i in range(a, 0, -1):
        print(i, end=" ")
def main():
    no = int(input("Enter a number: "))
    reverse(no)
    
if __name__ == "__main__":
    main()      