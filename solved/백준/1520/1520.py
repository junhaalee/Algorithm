import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]

dx,dy = [1,0,-1,0],[0,1,0,-1]

def dfs(x,y):
    
    if [x,y] == [n-1,m-1]:
        return 1

    if dp[x][y] != -1:    
        return dp[x][y]    

    dp[x][y] = 0

    for i in range(4):
        tx,ty = x+dx[i],y+dy[i]
        if (0<=tx<n) and (0<=ty<m) and graph[tx][ty] < graph[x][y]:
            dp[x][y] += dfs(tx,ty)

    return dp[x][y]

print(dfs(0,0))