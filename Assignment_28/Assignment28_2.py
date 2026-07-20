def CountWords(FileName):
    try:
        fobj = open(FileName,"r")

        Data = fobj.read()
        Words = Data.split()
        len1 =len(Words)

        fobj.close()
        return len1

    
    except FileNotFoundError as fobj:
        print("File is not present in directory")

def main():
        fname = input("Enter file name : ")
        Ret = CountWords(fname)
    
        print("Total number of words : ",Ret)


if __name__ == "__main__":
    main()