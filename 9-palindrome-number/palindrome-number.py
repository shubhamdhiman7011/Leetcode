class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reverse=str_x[::-1]
        if reverse==str(x):
         return True
        return False   
          
