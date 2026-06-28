def IsVowel(Chr):
    return (Chr=="a" or Chr=="e" or Chr=="i" or Chr=="o" or Chr=="u" or 
        Chr=="A" or Chr=="E" or Chr=="I" or Chr=="O" or Chr=="U")

def main():
    Char = input("Enter character:")
    if (IsVowel(Char)):
        print("Vowel")
    else:
        print("Not vowel")

if (__name__=="__main__"):
    main()