### LeetCode - [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

### 풀이

* any : 포함된 값 중 어느 하나가 참이면 return True 
* all : 포함된 모든 값이 True여야 return True

```Python

# 1. 나의 풀이
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for m in matrix:
            if (m[0] <= target <= m[-1]):
                index = bisect.bisect_left(m,target)
                if index < len(m) and m[index] == target:
                    return True
                    break
                    
        return False

# 2. Pythonic
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # any 사용
        return any(target in row for row in matrix)
```

