import copy
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

zero = []
for i in range(len(graph)):
    for k in range(len(graph[i])):
        if graph[i][k] == 0:
            zero.append([i,k])

zero_combi = list(combinations(zero,3))

def sol(graph, zc, n, m):

    t_graph = copy.deepcopy(graph)
    
    for x,y in zc:
        t_graph[x][y] = 1
    
    dx, dy = [1,0,-1,0],[0,-1,0,1]
    queue = deque()

    for x in range(n):
        for y in range(m):
            if t_graph[x][y] == 2:
                queue.append([x,y])
                while queue:
                    tx,ty = queue.popleft()
                    for i in range(4):
                        nx,ny = tx+dx[i], ty+dy[i]
                        if (0<=nx<n) and (0<=ny<m) and t_graph[nx][ny] == 0:
                            t_graph[nx][ny] = 2
                            queue.append([nx,ny])
    
    count = 0
    for i in range(len(t_graph)):
        for k in range(len(t_graph[i])):
            if t_graph[i][k] == 0:
                count += 1
    
    return count

result = 0
for zc in zero_combi:
    result = max(result, sol(graph,zc,n,m))
print(result)