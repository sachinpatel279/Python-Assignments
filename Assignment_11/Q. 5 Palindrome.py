def palindrome(no):
    num = no
    rev = 0
    while no > 0:
        rev = rev * 10 + no % 10
        no = no // 10
    
    if num == rev :
        return "Palindrome"
    else :
        return "Not palindrome"
         

def main():
    no =int(input("Enter number : "))
    ret = palindrome(no)
    print(ret)

if __name__ == "__main__":
    main()