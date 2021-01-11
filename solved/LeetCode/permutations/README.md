### LeetCode - [Permutations](https://leetcode.com/problems/permutations/)

### 풀이

* 재귀가 끝나면 호출한 바로 다음부터 다시 이어서 시작

```Python

# 1. from itertools import permuations
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums,len(nums))

# 2. DFS
class Solution:
    def permute(self, nums):
        
        result = []
        pre_elements = []
        
        def dfs(elements):
            # 더이상 추가할 원소가 없으면 result에 추가
            if len(elements) == 0:
                result.append(pre_elements[:])
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                pre_elements.append(e)
                dfs(next_elements)
                # dfs 종료시 마지막 원소제거 -> 그래야 pre가 123->12->1->13이 되는 재귀구조
                pre_elements.pop()
            
        dfs(nums)
        return result

```

