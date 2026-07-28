import os
import sys
import time
import re
import schedule

from DuplicateCodeLogic import DeleteDuplicate
from MailSender import SendMail

def CreateLogDirectory():

    DirectoryName = "Marvellous"

    if(os.path.exists(DirectoryName) == False):
        os.mkdir(DirectoryName)

    return DirectoryName


def CreateLogFile(LogDirectory):

    TimeStamp = time.strftime("%d_%m_%Y_%H_%M_%S")

    LogFileName = "DuplicateRemovalLog_"+TimeStamp+".log"

    LogFilePath = os.path.join(LogDirectory,LogFileName)

    fobj = open(LogFilePath,"w")

    return fobj,LogFilePath


def ValidateDirectory(DirectoryName):

    if(len(DirectoryName) == 0):
        return False

    if(os.path.isabs(DirectoryName) == False):
        return False

    if(os.path.exists(DirectoryName) == False):
        return False

    if(os.path.isdir(DirectoryName) == False):
        return False

    if(os.access(DirectoryName,os.R_OK) == False):
        return False

    if(os.access(DirectoryName,os.W_OK) == False):
        return False

    return True


def ValidateInterval(Interval):

    try:

        Interval = int(Interval)

        if(Interval <= 0):
            return False

        return True

    except Exception:

        return False

def ValidateEmail(Email):

    Pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if(re.match(Pattern,Email)):
        return True

    return False

def WriteLogHeader(fobj,DirectoryName):

    Border = "-" * 60

    StartTime = time.ctime()

    fobj.write(Border+"\n")
    fobj.write("Duplicate File Removal Automation\n")
    fobj.write(Border+"\n\n")

    fobj.write("Starting Time : "+StartTime+"\n")
    fobj.write("Directory Scanned : "+DirectoryName+"\n")
    fobj.write(Border+"\n\n")

    return StartTime


def DirectoryScanner(DirectoryName, ReceiverMail):

    LogDirectory = CreateLogDirectory()

    fobj, LogFileName = CreateLogFile(LogDirectory)

    StartTime = WriteLogHeader(fobj, DirectoryName)

    TotalFiles = 0
    DuplicateFound = 0
    DuplicateDeleted = 0

    Border = "-" * 60

    try:

        fobj.write("Scanning Started...\n\n")

        for FolderName, SubFolder, FileName in os.walk(DirectoryName):

            for fname in FileName:

                FilePath = os.path.join(FolderName, fname)

                TotalFiles = TotalFiles + 1

                fobj.write(FilePath + "\n")

        fobj.write("\n")
        fobj.write(Border + "\n")
        fobj.write("Duplicate File Information\n")
        fobj.write(Border + "\n\n")

        DuplicateFound, DuplicateDeleted = DeleteDuplicate(DirectoryName, fobj)

    except PermissionError as e:

        fobj.write("Permission Error : " + str(e) + "\n")

    except FileNotFoundError as e:

        fobj.write("File Error : " + str(e) + "\n")

    except Exception as e:

        fobj.write("Error : " + str(e) + "\n")

    EndTime = time.ctime()

    fobj.write("\n")
    fobj.write(Border + "\n")
    fobj.write("Operation Statistics\n")
    fobj.write(Border + "\n\n")

    fobj.write("Starting time of scanning : " + StartTime + "\n")

    fobj.write("Completion time of scanning : " + EndTime + "\n")

    fobj.write("Directory scanned : " + DirectoryName + "\n")

    fobj.write("Total number of files scanned : " + str(TotalFiles) + "\n")

    fobj.write("Total number of duplicate files found : " + str(DuplicateFound) + "\n")

    fobj.write("Total number of duplicate files deleted : " + str(DuplicateDeleted) + "\n")

    fobj.write(Border + "\n")

    return (fobj, LogFileName, StartTime, EndTime, TotalFiles, DuplicateFound, DuplicateDeleted)


def PerformOperation(DirectoryName, ReceiverMail):

    try:

        fobj, LogFileName, StartTime, EndTime, TotalFiles, DuplicateFound, DuplicateDeleted = DirectoryScanner(DirectoryName, ReceiverMail)


        SenderMail = input("Enter Sender Email : ")

        AppPassword = input("Enter App Password : ")


        Ret = SendMail(SenderMail, AppPassword, ReceiverMail, LogFileName, StartTime, EndTime, DirectoryName, TotalFiles, DuplicateFound, DuplicateDeleted)

        if(Ret == True):

            fobj.write("\n")
            fobj.write("Email Delivery Status : Success\n")

        else:

            fobj.write("\n")
            fobj.write("Email Delivery Status : Failed\n")

        fobj.close()

    except Exception as e:

        print("Error :",e)
########################################################
#
# Function Name : main
#
########################################################

def main():

    Border = "-" * 60

    print(Border)
    print("Duplicate File Removal Automation")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--help" or sys.argv[1] == "--h"):
            print("------------------------------------------------------------")
            print("Duplicate File Removal Automation")
            print("------------------------------------------------------------")
        
            print("This script scans a directory recursively,")
            print("identifies duplicate files using MD5 checksum,")
            print("deletes duplicate files,")
            print("creates a timestamp based log file,")
            print("and sends that log file through email.")
            print()
        
            print("Usage :")
            print("python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>")
            print()
        
            print("Example :")
            print("python DuplicateFileRemoval.py D:/Python/Demo 50 marvellousinfosystem@gmail.com")
            
            return

        elif(sys.argv[1] == "--usage" or sys.argv[1] == "--u"):
            print("Usage :")
            print("python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>")

            return

        else:

            print("Invalid Option")
            print("Use --help or --usage")
            return

    if(len(sys.argv) != 4):

        print("Invalid Number Of Arguments")
        print("Use --usage or --u")
        print("Use --help or --h")
        return

    DirectoryName = sys.argv[1]

    Interval = sys.argv[2]

    ReceiverMail = sys.argv[3]

    if(ValidateDirectory(DirectoryName) == False):

        print("Invalid Directory")
        return

    if(ValidateInterval(Interval) == False):

        print("Invalid Time Interval")
        return


    if(ValidateEmail(ReceiverMail) == False):

        print("Invalid Email Address")
        return

    PerformOperation(DirectoryName, ReceiverMail)

    schedule.every(int(Interval)).minutes.do(PerformOperation, DirectoryName, ReceiverMail)

    while True:
        schedule.run_pending()
        time.sleep(1)

########################################################
#
# Start Automation Script
#
########################################################

if __name__ == "__main__":
    main()