### LeetCode - [Array Partition I](https://leetcode.com/problems/array-partition-i)

### 풀이

* Pythonic Way

```Python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
```

