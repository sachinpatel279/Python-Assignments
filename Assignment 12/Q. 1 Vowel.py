
def CheckVowel(char):
    char = char.lower()
    if char in ("a","e","i","o","u"):
        return "Vowel"
    else:
        return "Consonant"

def main():
    char = input("Enter character : ")
    ret = CheckVowel(char)
    print(ret)

if __name__ == "__main__":
    main()