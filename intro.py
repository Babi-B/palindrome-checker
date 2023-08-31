from time import sleep

def intro():
    palindrome = ''

    print("")
    print("Hello and Welcome!")
    print("")
    print("This app is simple!")
    print("")
    print("You enter the word/phrase/sentence and we tell you if it is a palindrome or not")
    print("")
    palindrome = input("Please your text: ")
    print("")
    print("         Evaluating text. Please wait")
    print("")
    sleep(2)


    while palindrome == '':
        print("")
        print("         ! Sorry, an empty text is invalid")
        sleep(1)
        print("")
        palindrome = input("Please your text: ")
intro()



