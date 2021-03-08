import sys
import heapq
sys.setrecursionlimit(10000000)
from collections import deque
input = sys.stdin.readline

cnt = 1
while True:
    
    n = int(input())
    
    if not n:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    dp = [[sys.maxsize]*n for _ in range(n)]
    visit = [[0]*n for _ in range(n)]

    dx,dy = [1,0,-1,0],[0,1,0,-1]

    visit[0][0] = 1
    dp[0][0] = graph[0][0]

    queue = [[dp[0][0],0,0]]

    while queue:

        value, x, y = heapq.heappop(queue)

        if [x,y] == [n-1,n-1]:
            break

        for i in range(4):
            tx,ty = x+dx[i],y+dy[i]
            if (0<=tx<n) and (0<=ty<n) and visit[tx][ty] == 0:
                dp[tx][ty] = value+graph[tx][ty]
                heapq.heappush(queue, [dp[tx][ty],tx,ty])
                visit[tx][ty] = 1

    print("Problem "+str(cnt)+": "+str(dp[n-1][n-1]))
    cnt += 1
