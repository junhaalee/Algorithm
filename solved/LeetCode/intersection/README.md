### LeetCode - [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)

### 풀이

* Python은 다른 어떤 방법보다 모듈 이용하는게 제일 빠름

```Python

# 1. 내 풀이 - set.intersection()
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
```

