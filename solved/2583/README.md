### 백준 - [영역 구하기](https://www.acmicpc.net/problem/2583)

### 풀이

* DFS로 풀었음

```Python
def dfs(count,x,y,graph):
    global dx,dy
    count += 1
    graph[x][y] = 0
    for i in range(4):
        tx,ty = x+dx[i],y+dy[i]
        if (0<=tx<m) and (0<=ty<n) and graph[tx][ty] == 1:
            count = dfs(count,tx,ty,graph)
    return count
```

