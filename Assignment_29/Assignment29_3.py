import sys
def CopyContent(FileName1,FileName2):
    try: 
        FileName1 = sys.argv[1]
        FileName2 = sys.argv[2]

        fobj1 = open(FileName1,"r")
        fobj2 = open(FileName2,"w")

        Data = fobj1.read()
        fobj2.write(Data)
    
    except FileNotFoundError :
        print("File is not present in directory")
 
def main():
    fname1 = input("Enter first file name : ")
    fname2 = input("Enter second file name : ")
    CopyContent(fname1,fname2)

    print("Copy content of ",fname1, " into ",fname2)

if __name__ == "__main__":
    main()