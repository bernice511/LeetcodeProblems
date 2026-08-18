class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        for i in range(len(numbers)-1):
            sum = numbers[start] + numbers[end]
            if sum==target:
                return start+1, end+1
            elif sum<target:
                start=start+1
            else:
                end = end-1
            
                    