class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        l = 0
        for n in s:
            # current = n
            if (n-1) not in s:
                current = n
                current_l = 1
                while(current+1) in s:
                    current+=1
                    current_l+=1
                l = max(l,current_l)
        return l    
            



        