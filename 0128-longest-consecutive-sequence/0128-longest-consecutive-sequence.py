from collections import Counter 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        count=0
        max=0
        c=Counter(nums)
        x=list(c.keys())
        for i in range(1,len(x)):
            if x[i-1]+1 == x[i]:
                count+=1
            else:
                if max<count:
                    max=count
                count=0
        if max<count:
            max=count
        return max+1 if len(nums)!=0 else 0