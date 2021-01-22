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
        