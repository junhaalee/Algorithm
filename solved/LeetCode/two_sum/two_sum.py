nums = [2,7,11,15]
target = 9

# Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for k in range(i+1, len(nums)):
                if nums[i]+nums[k] == target:
                    return [i,k]

# target-n & in
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            # (0,2) (1,7) (2,11) (3,15)
            temp = target - n
            if temp in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(temp)+i+1]

# 첫번째 수를 뺀 결과 키 조회 - dictionary 사용
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i,n in enumerate(nums):
            dic[n] = i
        for i,n in enumerate(nums):
            if target-n in dic and i != dic[target-n]:
                return i, dic[target-n]