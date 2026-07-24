import schedule
import time
import datetime
import os

def  DirectoryScanner(DirectoryName):

    TotalFiles = 0
    TotalSubDirectories  = 0

    for FolderName, SubFolder , FileName in os.walk(DirectoryName):

        for fname in FolderName:
            TotalFiles = TotalFiles +1 
    
        for fsubname in SubFolder :
            TotalSubDirectories = TotalSubDirectories +1

    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p ")

    print("Directory Scanned :",DirectoryName)
    print("Total files : ",TotalFiles)
    print("Total SubDirectories : ",TotalSubDirectories)
    print("Scan time : ",timestamp)

def main():

    Directory = input("Enter directory name : ")
    DirectoryScanner(Directory)

    schedule.every(1).minute.do(DirectoryScanner, Directory)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()