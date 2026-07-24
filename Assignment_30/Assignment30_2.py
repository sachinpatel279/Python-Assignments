import schedule
import datetime
import time
def CurrentDateAndTime():

    currentdandt = datetime.datetime.now()
    print("Current Date and Time : ",currentdandt.strftime("%d-%m-%Y  %I:%M:%S %p"))

def main():

    schedule.every(1).minute.do(CurrentDateAndTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()