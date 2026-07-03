GreaterLength = lambda no : len(no) > 4

def main():
    data = ['hi', 'python', 'code', 'marvellous', 'ai']
    print("Input data is : ", data)
    fdata = list(filter(GreaterLength, data))
    print("data after filter : ", fdata)

if __name__ == "__main__":
    main()