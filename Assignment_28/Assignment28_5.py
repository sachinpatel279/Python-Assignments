import sys
def SearchWord(FileName,Word):
    try:

        fobj = open(FileName,"r")
        Data = fobj.read()

        if Word in Data :
            print(Word, " is presnt in ",FileName)
        else:
            print(Word," is not present in ",FileName)

        fobj.close()
        return Word

    except FileNotFoundError as fobj:
        print("File is not present in directory")

def main():
    fname = input("Enter file name : ")
    word = input("Enter word to search : ")

    SearchWord(fname,word)
    

if __name__ == "__main__":
    main()