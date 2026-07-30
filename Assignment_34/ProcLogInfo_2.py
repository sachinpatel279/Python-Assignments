########################################################
#
# File Name : ProcInfoLog.py
# Description : Process Log With Email Facility
# Author : Sachin Nemaram Patel
#
########################################################

import psutil
import sys
import os
import time
import re

from MailSender import SendMail

Border = "-" * 60

def ValidateDirectory(DirectoryName):

    try:

        if(len(DirectoryName) == 0):
            return False

        if(os.path.exists(DirectoryName) == False):
            os.mkdir(DirectoryName)

        if(os.path.isdir(DirectoryName) == False):
            return False

        return True

    except Exception:
        return False


def ValidateEmail(Email):

    Pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if(re.match(Pattern, Email)):
        return True

    return False

def CreateLogFile(DirectoryName):

    try:

        TimeStamp = time.strftime("%d_%m_%Y_%H_%M_%S")

        FileName = "ProcessLog_" + TimeStamp + ".log"

        FilePath = os.path.join(DirectoryName, FileName)

        fobj = open(FilePath, "w")

        return fobj, FilePath

    except Exception:

        return None, None


def WriteHeader(fobj):

    fobj.write(Border + "\n")
    fobj.write("Running Process Information\n")
    fobj.write(Border + "\n")
    fobj.write("Log Created At : " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")

def ProcessScan(fobj):

    Count = 0

    try:

        for proc in psutil.process_iter():

            try:

                Info = proc.as_dict(attrs=["pid","name","username"])

                Count = Count + 1

                fobj.write("PID : %s\n" % Info["pid"])
                fobj.write("Process Name : %s\n" % Info["name"])
                fobj.write("User Name : %s\n" % Info["username"])

                fobj.write(Border + "\n")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):

                pass

        return Count

    except Exception as e:

        fobj.write("Error : %s\n" % str(e))

        return 0

def PerformOperation(DirectoryName, ReceiverMail):

    try:

        fobj, LogFileName = CreateLogFile(DirectoryName)

        if(fobj == None):

            print("Unable to create Log File")
            return

        WriteHeader(fobj)

        TotalProcess = ProcessScan(fobj)

        fobj.write("\n")
        fobj.write(Border + "\n")
        fobj.write("Operation Statistics\n")
        fobj.write(Border + "\n")
        fobj.write("Total Running Processes : %d\n" % TotalProcess)
        fobj.write("Log Created At : %s\n" % time.ctime())
        fobj.write(Border + "\n")

        SenderMail = input("Enter Sender Email : ")

        AppPassword = input("Enter Gmail App Password : ")


        Ret = SendMail(SenderMail, AppPassword, ReceiverMail, LogFileName)

        if(Ret == True):

            fobj.write("Email Delivery Status : Success\n")

        else:

            fobj.write("Email Delivery Status : Failed\n")

        fobj.close()

    except Exception as e:

        print("Error :",e)


def DisplayHelp():

    print(Border)
    print("This automation script creates a log file")
    print("of all running processes and sends it through email.\n")
    print("Usage :")
    print("python ProcInfoLog.py DirectoryName ReceiverEmail \n")
    print("Example :")
    print("python ProcInfoLog.py Demo abc@gmail.com")
    print(Border)

def DisplayUsage():

    print("Usage :")
    print("python ProcInfoLog.py DirectoryName ReceiverEmail")

########################################################
#
# Function Name : main
#
########################################################

def main():

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--help" or sys.argv[1] == "--h"):

            DisplayHelp()
            return

        elif(sys.argv[1] == "--usage" or sys.argv[1] == "--u"):

            DisplayUsage()
            return

        else:

            print("Invalid Option")
            DisplayUsage()
            return

    if(len(sys.argv) != 3):

        print("Invalid Number Of Arguments")
        DisplayUsage()
        return


    DirectoryName = sys.argv[1]

    ReceiverMail = sys.argv[2]


    if(ValidateDirectory(DirectoryName) == False):

        print("Invalid Directory")
        return

    if(ValidateEmail(ReceiverMail) == False):

        print("Invalid Email Address")
        return


    PerformOperation(DirectoryName, ReceiverMail)

########################################################
#
# Application Starter
#
########################################################

if __name__ == "__main__":

    main()