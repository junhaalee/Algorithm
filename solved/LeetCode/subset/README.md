### LeetCode - [Subsets](https://leetcode.com/problems/subsets/)

### 풀이

* Combination Sum(./solved/LeetCode/combination_sum)과 유사한 문제

```Python

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def dfs(index, path):
            
            # 매번 결과 저장
            result.append(path)
            
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])
            
        dfs(0,[])
        
        return result

```

