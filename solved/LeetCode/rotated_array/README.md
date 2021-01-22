### LeetCode - [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

### 풀이

* index = bisect.bisect_left(nums,target)
* target의 index를 return(만약 target이 nums에 없을 경우, 가장 가까운 target보다 작은 수의 index를 return)

```Python
# 1. 나의 풀이
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        num = sorted(nums[:])
        index = bisect.bisect_left(num,target)
        
        if index < len(num) and num[index] == target:
            nums_dict = dict()
            for i,num in enumerate(nums):
                nums_dict[num] = i
            return nums_dict[target]

        else:
            return -1

# 2. list.index()
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        num = sorted(nums[:])
        index = bisect.bisect_left(num,target)
        
        if index < len(num) and num[index] == target:
            return nums.index(target)

        else:
            return -1

```

