import schedule
import time
import os
import shutil

def CopyFiles(SourceDirectory, DestinationDirectory):

    try:
        if os.path.isdir(SourceDirectory) == False:
            print("Source directory is not present with name : ",SourceDirectory)
            return

        if os.path.isdir(DestinationDirectory) == False:
            print("Destination directory is not present with name : ",DestinationDirectory)
            return

        LogFile = open("CopyLog.txt", "a")

        for fname in os.listdir(SourceDirectory):

            if fname.endswith(".txt"):

                SourcePath = os.path.join(SourceDirectory, fname)

                try:
                    shutil.copy(SourcePath, DestinationDirectory)

                    LogFile.write(fname + " copied successfully \n")
                    print(fname, "copied successfully")

                except Exception:
                    LogFile.write(fname + " not copied\n")
                    print(fname, "not copied")

        LogFile.close()

        print("Copy operation completed  \n")

    except Exception:
        print("Error occurred")

def main():

    SourceDirectory = input("Enter source directory : ")
    DestinationDirectory = input("Enter destination directory : ")

    schedule.every(10).minutes.do(CopyFiles, SourceDirectory, DestinationDirectory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()