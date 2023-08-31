# Remove whitespaces, punctuation, numbers etc
def clean_palindrome(palindrome):
    target = ''
    for pal in palindrome:
        if pal.isalpha():
            target += pal
    return target