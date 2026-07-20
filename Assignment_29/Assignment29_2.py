def FileContents(FileName):
    try:        
        fobj = open(FileName,"r")
        Data = fobj.read()
        fobj.close()
        return Data
    
    except FileExistsError as fobj:
        print("File is not present in direcotry")
    
def main():
    fname = input("Enter file name : ")
    Ret = FileContents(fname)
    print(Ret)
    
if __name__ == "__main__":
    main()