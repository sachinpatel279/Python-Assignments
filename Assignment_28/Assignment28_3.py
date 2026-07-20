def DisplayFile(FileName):
    try:
        fobj = open(FileName,"r")

        for fline in fobj:
            print(fline,end = "")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not present in directory")
    
def main():
        
        fname =input("Enter file name : ")
        DisplayFile(fname)
        

if __name__ == "__main__":
    main()