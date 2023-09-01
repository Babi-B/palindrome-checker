from intro import intro
from clean_palindrome import clean_palindrome

def checker():
    isPalindrome = True
    tracker = 0

    # Get the palindrome from the intro module
    palindrome = intro()
    target = clean_palindrome(palindrome)

    # Get the turning point
    mid_indx = round(len(target) / 2)
    # pivot = target[mid_indx]
    x = y = mid_indx


    while x < len(target)  and y > 0 and isPalindrome:
        x += 1
        y -= 1
        print(f"{target[x]}, {target[y]}")
        if target[x] == target[y]:
            tracker += 1
            isPalindrome = True
        else:
            isPalindrome = False

    print(f"Your text, {palindrome}, is a palindrome") if (isPalindrome and tracker == mid_indx) else print(f"Your text, {palindrome}, is not a palindrome")


