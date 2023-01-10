# class Solution:
#     def isPalindrome(self, x: int) -> bool:

x = str(input("What is the value of x? "))
stringnumber = x[::-1]

if stringnumber == x:
    print("True")
else:
    print("False")