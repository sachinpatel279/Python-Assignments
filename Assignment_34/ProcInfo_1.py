########################################################
#
# File Name : ProcInfo_1.py
# Description : Display Running Process Information
# Author : Sachin Nemaram Patel
#
########################################################

import psutil
import sys

Border = "-" * 60

def ProcessDisplay():

    try:

        print(Border)
        print("---- Running Process Information ----")
        print(Border)

        for proc in psutil.process_iter():

            try:

                Info = proc.as_dict(attrs=["pid","name","username"])

                print("PID           :", Info["pid"])
                print("Process Name  :", Info["name"])
                print("User Name     :", Info["username"])

                print(Border)

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):

                pass

    except Exception as e:

        print("Error :",e)

def DisplayHelp():

    print(Border)
    print("This script displays information of all running processes.")
    print()
    print("Usage :")
    print("python ProcInfo_1.py")
    print(Border)

def DisplayUsage():

    print("Usage : python ProcInfo_1.py")

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
            return

    if(len(sys.argv) != 1):

        print("Invalid Number Of Arguments")
        DisplayUsage()
        return

    ProcessDisplay()

########################################################
#
# Application Starter
#
########################################################

if __name__ == "__main__":

    main()