import schedule
import datetime
import time
import os

def MonitorFileSize():
    Border = "="*40

    FileName = "FileSizeLog.txt"
    timeStamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    FileExists = os.path.exists(FileName)
    if(FileExists == False):
        print("File is exists in directory with name : ",FileName)
        return 

    FileSize = os.path.getsize(FileName)

    fobj = open(FileName,"a")

    fobj.write(Border + "\n")

    fobj.write(f"File path : {FileName} \n")
    fobj.write(f"File size : {FileSize} \n")
    fobj.write(f"Date and time : {timeStamp} \n")

    fobj.write(Border + "\n")

    fobj.close()

def main():

    schedule.every(30).seconds.do(MonitorFileSize)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()