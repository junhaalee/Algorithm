class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

class Solution:
    def majorityElement(self, nums):
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums)//2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])
        print(a,b)
        print(nums)
        print(nums.count(a) > half)
        print([b,a][nums.count(a) > half])
        print()
        return [b,a][nums.count(a) > half]
s = Solution()

print(s.majorityElement([2,2,1,1,1,2,2]))