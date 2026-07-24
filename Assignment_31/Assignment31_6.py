import schedule
import datetime
import time

def MondaySchedule():

    print("Monday 9:00 AM : Start your weekly goals")

def WednesdaySchedule():

    print("Wednesday 5:00 PM : Review your weekly progress")

def FridaySchedule():

    print("Friday 6:00 PM : Weekly work completed")

def main():

    MondaySchedule()
    WednesdaySchedule()
    FridaySchedule()

    schedule.every().monday.at("09:00").do(MondaySchedule)
    schedule.every().wednesday.at("17:00").do(WednesdaySchedule)
    schedule.every().friday.at("18:00").do(FridaySchedule)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()