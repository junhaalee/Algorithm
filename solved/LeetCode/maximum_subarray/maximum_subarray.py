nums = [-2,1,-3,4,-1,2,1,-5,4]
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -sys.maxsize
        current = 0

        for num in nums:
            current = max(current+num, num)
            result = max(result, current)
        
        return nums


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for i in range(1, len(nums)):
            dp.append(max(dp[i-1]+nums[i], nums[i]))
        
        return max(dp)
