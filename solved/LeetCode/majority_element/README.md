### LeetCode - [Majority Element](https://leetcode.com/problems/majority-element/)

### 풀이

* 분할정복 풀이
* 정렬을 이용한 풀이

```Python
# 정렬
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

# 분할정복
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums)//2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b,a][nums.count(a) > half]
```

* True : 1 / False : 0