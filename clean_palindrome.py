# Remove whitespaces, punctuation, numbers etc
def clean_palindrome(palindrome):
    target = ''
    for pal in palindrome:
        if pal.isalpha() or pal.isdigit():
            target += pal
    return target