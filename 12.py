def isPalindrome(s): 
    return s == s[::-1] 
  
if __name__ == "__main__":
    s = input('enter a string to check palindrome ')
    ans = isPalindrome(s) 
  
    if ans: 
        print("Yes") 
    else: 
        print("No")