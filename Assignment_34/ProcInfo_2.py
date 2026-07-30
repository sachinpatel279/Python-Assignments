########################################################
#
# File Name : ProcInfo_2.py
# Description : Display Information Of Specific Process
# Author : Sachin Nemaram Patel
#
########################################################

import psutil
import sys

Border = "-" * 60

def ProcessDisplay(ProcessName):

    Found = False

    try:

        for proc in psutil.process_iter():

            try:

                Info = proc.as_dict(attrs=["pid","name","username"])

                if(Info["name"] != None):

                    if(Info["name"].lower() == ProcessName.lower()):

                        Found = True

                        print(Border)
                        print("Process Information")
                        print(Border)

                        print("PID           :", Info["pid"])
                        print("Process Name  :", Info["name"])
                        print("User Name     :", Info["username"])

                        print(Border)

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):

                pass

        if(Found == False):

            print("Process is not running.")

    except Exception as e:

        print("Error :",e)

def DisplayHelp():

    print(Border)
    print("This script displays information of a running process.")
    print()
    print("Usage :")
    print("python ProcInfo_2.py ProcessName")
    print()
    print("Example :")
    print("python ProcInfo_2.py notepad.exe")
    print(Border)

def DisplayUsage():

    print("Usage : python ProcInfo_2.py ProcessName")

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

        ProcessName = sys.argv[1]

        ProcessDisplay(ProcessName)

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