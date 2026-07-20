def CopyFile(FileName1,FileName2):
    try:
        
        fobj1 = open(FileName1,"r")
        fobj2 = open(FileName2,"w")

        Data =fobj1.read()
        fobj2.write(Data)

        fobj1.close()
        fobj2.close()

        return FileName1,FileName2

    except FileNotFoundError :
        print("File is not present in directory")

def main():
    try:
        fname1 = input("Enter first file name : ")
        fname2 = input("enter second file name : ")       
        Ret = CopyFile(fname1,fname2)

        print("Content of ",fname1, " copied into ",fname2)

    except FileNotFoundError :
        print("File is not present in directory")

if __name__ == "__main__":
    main()