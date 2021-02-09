nums = [2,1,1,2]

a = nums[1::2]

nums = [1,2,3,1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        dp = [nums[0],max(nums[0],nums[1])]
        for i in range(2, len(nums)):
            dp.append(max(dp[i-1], dp[i-2]+nums[i]))
        
        return max(dp[-1],dp[-2])

