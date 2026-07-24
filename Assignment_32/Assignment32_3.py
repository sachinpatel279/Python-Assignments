import schedule
import time

def Display(FileName):
    try:
        fobj = open(FileName,"r")

        data =fobj.read()

        if data == "":
            print("File is empty")
        else:
            print(data)

        fobj.close()

    except FileNotFoundError:
        print("File is not exists with name ",FileName)

    except PermissionError:
        print("Permission denied")

    except OSError:
        print("File cannot be opened")

def main():
    fname = input("Enter file name: ")
    schedule.every(1).minute.do(Display,fname)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()