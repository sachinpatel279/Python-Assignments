import schedule
import time
import datetime

def CreateLogFile():

    timeStamp =datetime.datetime.now()

    LogFile = "MarvellousLog_"+ timeStamp.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(LogFile,"w")

    fobj.write("Log file created successfully.")
    fobj.write("Creation time : ")
    fobj.write(timeStamp.strftime("%d-%m-%Y %I:%M:%S %p \n"))

    fobj.close()

def main():
    CreateLogFile()

    schedule.every(10).minutes.do(CreateLogFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()