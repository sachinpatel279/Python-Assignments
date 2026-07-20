import os

def FileExists(FileName):
    if(os.path.exists(FileName)):
        print(FileName," file is exists ")
    else:
        print(FileName," file is not exists")

def main(): 
    fname = input("Enter file name : ")
    FileExists(fname)

if __name__ =="__main__":
    main()