import schedule
import time
import os

def DeleteEmptyFiles(Directory):

    DirectoryPath = False

    DirectoryPath = os.path.exists(Directory)
    if(DirectoryPath == False):
        print("This directory not exists with name : ",Directory)
        return

    DirectoryPath = os.path.isdir(Directory)

    if(DirectoryPath == False):
        print("It is not a directory with name : ",Directory)
        return

    fobj = open("DeleteLogFile.txt","a")

    for FolderName, SubFolder, FileName in os.walk(Directory):
        for fname in FileName:

            if fname == "DeleteLogFile.txt":
                continue

            fname = os.path.join(FolderName, fname)

            if os.path.getsize(fname) == 0:

                os.remove(fname)

                print(fname, "Deleted Successfully")

                fobj.write(fname + "\n")

    fobj.close()

def main():

    dname = input("Enter directory path : ")

    schedule.every(1).minute.do(DeleteEmptyFiles,dname)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()