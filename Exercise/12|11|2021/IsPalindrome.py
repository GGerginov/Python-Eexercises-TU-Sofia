def isPalindrome(s):
    return int(bool(s == s[::-1]))

input = input("Check is palindrome:")

print(isPalindrome(input))

