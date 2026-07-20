def CountLines(FileName):
    try:
        fobj = open(FileName, "r")

        count = 0
        for i in fobj:
            count = count + 1

        fobj.close()
        return count
    
    except FileNotFoundError as fobj:
        print("File is not present in directory")

def main():
        
    fname = input("Enter file name : ")
    Ret = CountLines(fname)
    print("Total Number of lines in ", fname, " is : ", Ret)

if __name__ == "__main__":
    main()