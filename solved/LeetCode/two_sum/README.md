### LeetCode - [Two Sum](https://leetcode.com/problems/two-sum)

### 풀이

* 배열 : index()를 통해서 index를 조회
* Dictionary : enumerate과 key를 통해서 index를 조회

```Python

# 1. 나의 풀이 : Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                if nums[i]+nums[k] == target:
                    return [i,k]


# 2. target-n & in 을 통한 탐색
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            # (0,2) (1,7) (2,11) (3,15)
            temp = target - n
            if temp in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(temp)+i+1]


# 3. 첫번째 수를 뺀 결과 키 조회
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i,n in enumerate(nums):
            dic[n] = i
        for i,n in enumerate(nums):
            if target-n in dic and i != dic[target-n]:
                return i, dic[target-n]
```
* 2번에서는 target-n의 index를 .index()로 찾았고, 3번에서는 dic type을 통해서 '키'로 조회