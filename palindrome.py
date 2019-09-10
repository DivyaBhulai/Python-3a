def palindrome(txt):
    if (txt == txt[::-1]):
        print(True)
    else:
        print(False)

palindrome("racecar")

