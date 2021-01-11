nums = [1,2,3]

class Solution:
    def permute(self, nums):
        
        result = []
        pre_elements = []
        
        def dfs(elements):
            print(pre_elements, elements)
            if len(elements) == 0:
                result.append(pre_elements[:])
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                pre_elements.append(e)
                dfs(next_elements)
                print('dfs 끝')
                pre_elements.pop()
            
        dfs(nums)
        return result
    
sol = Solution()
a = sol.permute(nums)