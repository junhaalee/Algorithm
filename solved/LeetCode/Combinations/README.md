### LeetCode - [Combintations](https://leetcode.com/problems/combinations/)

### 풀이

* 속도는 from itertools import combinations가 훨-씬 빠-름

```Python

# 1. from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1,n+1),k))

# 2. DFS
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        results = []

        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])
            
            # 순열은 자신을 제외하고 모든 요소를 next_elements로 처리했지만
            # 조합은 자기 자신뿐만 아니라 앞의 모든 요소를 배제하고 next_elements(elements) 구성.
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
            
        dfs([], 1,k)
        
        return results
```

