import schedule
import time
import datetime
import os
import shutil


def BackupProgram(SourceFile, DestinationFile):
    
    timeStamp = datetime.datetime.now()

    sourceFileName = os.path.basename(SourceFile)

    FileName = os.path.splitext(sourceFileName)[0]
    Extension = os.path.splitext(sourceFileName)[1]

    BackupFile = FileName + "_" + timeStamp.strftime("%d_%m_%Y_%H_%M_%S") + Extension

    Ret = os.path.exists(SourceFile)

    if(Ret == False):
        print("Source file does not exist")
        return

    Ret = os.path.exists(DestinationFile)

    if(Ret == False):
        print("Destination directory does not exist")
        return

    Ret = os.path.isdir(DestinationFile)

    if(Ret == False):
        print(DestinationFile, "is not a directory")
        return

    for FolderName, SubFolder, FileName in os.walk(DestinationFile):

        DestinationFile = os.path.join(FolderName, BackupFile)

        shutil.copy(SourceFile, DestinationFile)

        fobj = open("backup_log.txt", "a")

        fobj.write("Backup completed successfully at : ")
        fobj.write(timeStamp.strftime("%d-%m-%Y %I:%M:%S %p \n"))

        fobj.close()

        print("Backup completed successfully")
        print("Backup File :", BackupFile)

def main():

    source = input("Enter source file path : ")
    destination = input("Enter destination directory : ")

    schedule.every(1).hour.do(BackupProgram, source, destination)

    print("Backup Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()