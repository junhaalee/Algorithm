### 백준 - [1520](https://www.acmicpc.net/problem/1520)

### 풀이

* 단순히 DFS, BFS만 이용하면, 최적의 경로를 찾는 문제가 아니기 때문에 시간초과가 난다.
* DFS+DP 또는 BFS+PQ로 풀어야한다는데, 나는 DFS+DP로 풀었다.

* 재귀를 활용할 때에는 setrecursionlimit을 잊지말것.

```Python

def dfs(x,y):
    
    if [x,y] == [n-1,m-1]:
        return 1

    if dp[x][y] != -1:    
        return dp[x][y]    

    dp[x][y] = 0

    # 일단 목적지에 도착한 이후에
    # 출발지로 다시 거슬러올라가면서 DP 안의 값들을 더해주는 방식
    for i in range(4):
        tx,ty = x+dx[i],y+dy[i]
        if (0<=tx<n) and (0<=ty<m) and graph[tx][ty] < graph[x][y]:
            dp[x][y] += dfs(tx,ty)

    return dp[x][y]

```

