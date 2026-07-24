import schedule
import time
def IntervalMessage(MyMessage,TimeInterval):

        if(TimeInterval < 1):
             print("Interval should be greater than zero")
             return
        else:
             print(MyMessage)

def main():

    Message = input("Enter Message : ")
    Inteval = int(input("Enter interval in seconds : "))

    IntervalMessage(Message,Inteval)
    
    schedule.every(Inteval).seconds.do(IntervalMessage, Message,Inteval)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()