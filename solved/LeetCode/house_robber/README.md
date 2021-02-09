### LeetCode - [House Robber](https://leetcode.com/problems/house-robber/)

### 풀이

```Python

# 내 풀이
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
```