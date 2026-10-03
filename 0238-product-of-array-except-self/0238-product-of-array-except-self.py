class Solution:
    def productExceptSelf(self, nums: List[int]):
        # pref = 1
        # prod_list = [1]*len(nums)
        # suf = 1
        # for i in range(len(nums)):
        #     if i!=0:
        #         pref *=nums[i-1]
        #         prod_list[i] *= pref
        #     if i!=len(nums)-1:
        #         suf *= nums[len(nums)-i-1]
        #         prod_list[len(nums)-1-i-1] *= suf

        # return prod_list

        n = len(nums)
        res = [1]* n
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(n-1,-1,-1):
            res[i] *= right
            right *= nums[i]
        return res

