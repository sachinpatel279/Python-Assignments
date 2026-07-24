import schedule
import time
from datetime import datetime

def CreatesNewFile():
    timeStamp = datetime.now()

    FileName = "File_" + timeStamp.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(FileName,"w")

    fobj.write(f"File Name : {FileName} \n")
    fobj.write(f"Creation date : {timeStamp.strftime("%d-%m-%Y")} \n")
    fobj.write(f"Creation time : {timeStamp.strftime("%I:%M:%S:%p")}\n")

    fobj.close()

def main():

    schedule.every(1).minute.do(CreatesNewFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()