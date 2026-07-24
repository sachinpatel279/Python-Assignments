import schedule
import time
import datetime
def EntryIntoFile():

    fobj = open("Marvellous.txt","a")

    timedate = datetime.datetime.now()

    fobj.write("Task executed at : ")
    fobj.write(timedate.strftime("%d-%m-%Y %I:%M:%S %p \n"))

    fobj.close()

def main():
    
    schedule.every(5).minutes.do(EntryIntoFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()