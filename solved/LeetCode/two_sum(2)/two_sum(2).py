numbers = [2,7,11,15]
target = 9

# 투 포인터 - 64ms
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

# 이진 검색 - 1116ms
import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            result = bisect.bisect_left(numbers[i+1:], target-num)
            if result+i+1 < len(numbers) and numbers[i]+numbers[result+i+1] == target:
                return [i+1, result+i+2]


