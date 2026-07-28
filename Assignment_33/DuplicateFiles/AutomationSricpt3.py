import sys

def main():

    if(len(sys.argv) == 2): #command 2 dile astil tar aat janar
        if(sys.argv[1]== "--h" or sys.argv[1]== "--H"):
            print("Help")
        elif(sys.argv[1]== "--u" or sys.argv[1]== "--U"):
            print("Usage")
        else:    
            DirectoryName = sys.argv[1]
            print("Directory name is : ",DirectoryName)
    else:
        print("Invalid number of arguments")
        print("please use --h or --u for more information")

if __name__ =="__main__":
    main()