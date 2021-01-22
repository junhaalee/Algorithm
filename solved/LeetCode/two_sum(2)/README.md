### LeetCode - [Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

### 풀이

* numbers가 정렬되어 있을 경우에만, 투포인터 가능
* 모듈이 항상 더 빠른건 아니다....
* 가 아니였다. 모듈은 빠르다.

```Python

# 1. 내 풀이 - 투 포인터 - 64ms
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0,len(numbers)-1

        while left <= right:

            if numbers[left]+numbers[right] < target:
                left += 1
            elif numbers[left]+numbers[right] > target:
                right -= 1
            else:
                return [left+1,right+1]
        
# 2. Binary Search - 1116ms
import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            result = bisect.bisect_left(numbers[i+1:], target-num)
            if result+i+1 < len(numbers) and numbers[i]+numbers[result+i+1] == target:
                return [i+1, result+i+2]

# 3. 슬라이싱을 사용하지 않는 Binary Search
import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            # bisect_left(nums, target, lo=0, hi=len(a))
            # i+1을 parameter로 추가해줌으로써, 왼쪽 범위에 제한을 줄 수 있음
            result = bisect.bisect_left(numbers, target-num, i+1)
            if result < len(numbers) and numbers[i]+numbers[result] == target:
                return [i+1, result+1]
```

