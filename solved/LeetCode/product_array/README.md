### LeetCode - [Product of Array Excpet Self](https://leetcode.com/problems/product-of-array-except-self/)

### 풀이

* 나눗셈 금지 / O(n)에 풀 수 있는 방법 : 왼쪽 곱 * 오른쪽 곱

```Python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []

        # 왼쪽 곱
        p = 1
        for i in range(len(nums)):
            ans.append(p)
            p *= nums[i]
        
        # 오른쪽 곱
        p = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= p
            p *= nums[i]
        
        return ans
```

