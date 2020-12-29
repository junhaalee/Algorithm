import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x,y,k):

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if (0 <= tx < n) and (0 <= ty < n) and visit[tx][ty] and graph[tx][ty] > k:
            visit[tx][ty] = 0
            dfs(tx,ty,k)

ans = 0

for k in range(max(map(max,graph))):
    visit = [[1]*n for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(n):
            if visit[x][y] and graph[x][y] > k:
                count += 1
                visit[x][y] = 0
                dfs(x,y,k)
    ans = max(ans, count)

print(ans)