### 백준  - [2667](https://www.acmicpc.net/problem/2667)

### 풀이

* DFS // 문제에 맞는 알고리즘을 만들어줄것!

```Python
def dfs(x,y,graph,visit,n):
    if x>=0 and y>=0 and x<n and y <n and graph[x][y] and [x,y] not in visit:
        visit.append([x,y])
        graph[x][y] = 0
        if x+1 <= n:
            visit = dfs(x+1,y,graph,visit,n) 
        if y+1 <= n:
            visit = dfs(x,y+1,graph,visit,n) 
        visit = dfs(x-1,y,graph,visit,n) 
        visit = dfs(x,y-1,graph,visit,n)
    return visit
```

