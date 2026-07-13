
def MultiplicationTable(no):
    for i in range(1,11):
        print(no * i)

def main():
    no = int(input("Enter a number : "))
    MultiplicationTable(no)
    
if __name__=="__main__":
    main()

