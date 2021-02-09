### LeetCode - [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

### 풀이

* 카데인 알고리즘 : 단계별 최적의 해를 통해 전체 최적의 해를 구하는 알고리즘

```Python

# 카데인 알고리즘
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -sys.maxsize
        current = 0

        for num in nums:
            current = max(current+num, num)
            result = max(result, current)
        
        return nums


# DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for i in range(1, len(nums)):
            dp.append(max(dp[i-1]+nums[i], nums[i]))
        
        return max(dp)
```

