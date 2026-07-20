import sys
def CompareFiles(FileName1,FileName2):
    try:
        FileName1 = sys.argv[1]
        FileName2 = sys.argv[2]

        fobj1 = open(FileName1,"r")
        fobj2 = open(FileName2,"r")

        Data1=fobj1.read()
        Data2=fobj2.read()

        if Data1 == Data2:
            print("Success")
        else:
            print("Failure")

        fobj1.close()
        fobj2.close()
            
    except FileNotFoundError:
        print("File is not present in directory")

def main():
    fname1 = input("Enter first file name : ")
    fname2 = input("Enter second file name : ")
    CompareFiles(fname1,fname2)

if __name__ =="__main__":
    main()