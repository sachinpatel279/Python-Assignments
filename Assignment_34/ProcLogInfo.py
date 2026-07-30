########################################################
#
# File Name : ProcInfoLog.py
# Description : Create Log File Of Running Processes
# Author : Sachin Nemaram Patel
#
########################################################

import psutil
import sys
import os
import time

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


def CreateLogFile(DirectoryName):

    try:

        TimeStamp = time.strftime("%d_%m_%Y_%H_%M_%S")

        FileName = "ProcessLog_" + TimeStamp + ".log"

        FilePath = os.path.join(DirectoryName, FileName)

        fobj = open(FilePath, "w")

        return fobj

    except Exception:

        return None


def WriteLogHeader(fobj):

    fobj.write(Border + "\n")
    fobj.write("Running Process Information\n")
    fobj.write(Border + "\n")
    fobj.write("Log Created At : " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")

def ProcessScan(fobj):

    try:

        for proc in psutil.process_iter():

            try:

                Info = proc.as_dict(attrs=["pid","name","username"])

                fobj.write("PID : %s\n" % Info["pid"])
                fobj.write("Process Name : %s\n" % Info["name"])
                fobj.write("User Name : %s\n" % Info["username"])
                fobj.write(Border + "\n")

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):

                pass

    except Exception as e:

        fobj.write("Error : %s\n" % str(e))


def DisplayHelp():

    print(Border)
    print("This automation script creates a log file")
    print("which contains information of all running processes.")
    print()
    print("Usage :")
    print("python ProcInfoLog.py DirectoryName")
    print()
    print("Example :")
    print("python ProcInfoLog.py Demo")
    print(Border)

def DisplayUsage():

    print("Usage : python ProcInfoLog.py DirectoryName")

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

        DirectoryName = sys.argv[1]

        Ret = ValidateDirectory(DirectoryName)

        if(Ret == False):

            print("Invalid Directory")
            return


        fobj = CreateLogFile(DirectoryName)

        if(fobj == None):

            print("Unable to create log file")
            return
        
        WriteLogHeader(fobj)
        ProcessScan(fobj)

        fobj.write(Border + "\n")
        fobj.write("End Of Log File\n")
        fobj.write(Border + "\n")

        fobj.close()

        print("Log File Created Successfully")

    else:

        print("Invalid Number Of Arguments")
        DisplayUsage()

########################################################
#
# Application Starter
#
########################################################

if __name__ == "__main__":
    main()