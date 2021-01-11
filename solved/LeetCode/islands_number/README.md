### LeetCode - [Number of Islands](https://leetcode.com/problems/number-of-islands/)

### 풀이

```Python

# 1. recursive DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x,y):
            # 땅이 아닌 부분을 만나면 break
            if x < 0 or y < 0 or x > len(grid) or y > len(grid[0]) or grid[x][y] != '1':
                return
            
            # 방문한 땅은 '1'이 아닌 다른 문자로 수정
            grid[x][y] = 0

            # 동서남북 탐색
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                # 땅이라면 탐색 시작
                if grid[x][y] == '1':
                    dfs(x,y)
                    # 탐색 끝났으면 섬 하나 찾을 것과 동일한 의미이므로 count += 1
                    count += 1

        return count
```

