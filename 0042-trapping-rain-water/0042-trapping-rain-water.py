class Solution:
    def trap(self, height: list[int]) -> int:
        start = 0
        end = len(height)-1
        left_max = 0
        right_max = 0
        water = 0
        while start<end:
            left_max = max(left_max, height[start])
            right_max = max(right_max, height[end])

            if left_max<right_max:
                water += left_max-height[start]
                start+=1
            else:
                water += right_max-height[end]
                end-=1
        return water