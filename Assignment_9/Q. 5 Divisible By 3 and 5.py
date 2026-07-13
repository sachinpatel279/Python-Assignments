
def Divisible(no):
    if no%3==0 and no%5==0 :
        return " Divisible by 3 and 5 "
    else :
        return " Not divisible by 3 and 5" 

def main():
    no = int(input("Enter number : "))
    Divisible(no)
    ret = Divisible(no)
    print(no, ret)

if __name__ == "__main__":
    main()