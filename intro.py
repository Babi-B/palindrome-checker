from time import sleep

palindrome = ''

def intro():
    

    print("")
    print("         Hello and Welcome!")
    print("")
    print("         This app is simple!")
    print("")
    print("     You enter the word/phrase/sentence and we tell you if it is a palindrome or not")
    print("")
    palindrome = input("Please enter your text: ")
    print("")
    print("         Evaluating text. Please wait")
    print("")
    sleep(1)

    # Do not enter an empty string
    while palindrome == '':
        print("")
        print("         ! Sorry, an empty text is invalid")
        sleep(1)
        print("")
        palindrome = input("Please enter your text: ")
    
    while palindrome.isdigit():
        print("")
        print("         ! Sorry, an empty text is invalid. Text with ALPHABETS only")
        sleep(1)
        print("")
        palindrome = input("Please enter your text: ")
    return palindrome
