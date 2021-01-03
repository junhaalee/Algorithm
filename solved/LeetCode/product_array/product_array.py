nums = [1,2,3,4]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []

        p = 1
        for i in range(len(nums)):
            ans.append(p)
            p *= nums[i]
        
        p = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= p
            p *= nums[i]
        
        return ans