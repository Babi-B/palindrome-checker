from intro import intro

def checker():
    # Get the palindrome from the intro module
    palindrome = intro()
    target = clean_palindrome(palindrome)
        
    # target = palindrome.replace(" ","")
    print("")
    print(f"This is a {target}")


# Remove whitespaces, punctuation, numbers etc
def clean_palindrome(palindrome):
    target = ''
    for pal in palindrome:
        if pal.isalpha():
            target += pal
    return target