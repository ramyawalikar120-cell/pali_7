import sys
def isPalindrome(s): 
    return s == s[::-1]
    if __name__ == "__main__": 
        string = sys.argv[1] 
        if isPalindrome(string): 
            print("The string is a palindrome")
    else: 
            print("The string is not a palindrome") 
