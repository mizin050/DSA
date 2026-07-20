class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        
        x=[]
        for i in s:
            if i.isalpha() or i.isdigit():
                x.append(i.lower()) 
        print(x)
        right=len(x)-1
        while left<right:
            if x[left] != x[right]:
                return False
            left+=1
            right-=1
        return True
        