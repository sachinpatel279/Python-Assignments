import schedule
def EveryDay():
    
    print("Namskar")

def main():

    schedule.every().day.at("9:00").do(EveryDay)

if __name__ == "__main__":
    main()