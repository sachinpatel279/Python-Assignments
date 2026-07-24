import schedule
import time

def Schedules():

    print("Coding kar...!")


def main():

    schedule.every(30).minutes.do(Schedules)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()