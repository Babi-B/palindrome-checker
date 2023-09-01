from intro import intro
from clean_palindrome import clean_palindrome

def checker():
    # First asumption: the text is a palindrome
    isPalindrome = True

    # Counts the number of comparisons
    tracker = 0

    # Get the palindrome from the intro module
    palindrome = intro()
    target = clean_palindrome(palindrome)

    # Get the turning point
    mid_indx = round(len(target) / 2)
    # pivot = target[mid_indx]
    x = y = mid_indx


    while x < len(target)  and y > 0 and isPalindrome:
        # start with the number AFTER the midpoint and move to the end
        x += 1

        # start with the number BEFORE the midpoint and move to the start
        y -= 1

        if target[x] == target[y]:
            tracker += 1
        else:
            isPalindrome = False
            
    # The number of comparisons should be equal to the midpoint
    print(f"Your text, {palindrome}, is a palindrome") if (isPalindrome and tracker == mid_indx) else print(f"Your text, {palindrome}, is not a palindrome")


