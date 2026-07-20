def FrequencyofString(FileName,Fstring):
    try:
        fobj = open(FileName,"r")
        Data = fobj.read()

        Count = 0
        for Data in FileName:
             Count = Count + 1
        fobj.close()

        return Count
    
    except FileNotFoundError as fobj:
        print("file is not present in directory")

def main():
    
        fname = input("Enter file name : ")
        fstring = input("Enter a string :")
        ret = FrequencyofString(fname,fstring)
        print("Frequency of ",fstring," is ", ret)

if __name__ =="__main__":
    main()