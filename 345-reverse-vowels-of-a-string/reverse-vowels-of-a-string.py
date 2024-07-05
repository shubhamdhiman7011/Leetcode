class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        shub1=list(s)
        n=len(shub1)
        left,right=0,n-1
        while left<right:
           while left<right and shub1[left] not in vowels:
            left+=1
           while left<right and shub1[right] not in vowels: 
            right-=1
           if left<right:
            shub1[left],shub1[right]=shub1[right],shub1[left]
            left+=1
            right-=1
        return "".join(shub1)    