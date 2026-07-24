import schedule
import time
import datetime
import os

def DirectoryCount(DirectoryName):

    timeStamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p \n")

    TotalFiles = 0

    DirectoryPath = os.path.exists(DirectoryName)
    if(DirectoryPath == False):
        print("Directory does not exists with name : ",DirectoryName)
        return

    DirectoryPath = os.path.isdir(DirectoryName)
    if(DirectoryPath == False):
        print("It is not directory with name : ",DirectoryName)
        return
    
    
    for FolderName,SubFolder,FileName in os.walk(DirectoryName):

        for fname in FileName:
            TotalFiles = TotalFiles + 1

    print("Directory Name : ",DirectoryName)
    print("Total Files : ", TotalFiles)

    fobj= open("DirectoryCountLog.txt","a")

    fobj.write(f"Directory Path : {DirectoryName}\n")
    fobj.write(f"Number of files : {TotalFiles}\n")
    fobj.write(f"Date and Time : {timeStamp}\n")

    fobj.close()

def main():
    Directory = input("Enter directory name : ")

    schedule.every(5).minutes.do(DirectoryCount,Directory)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()