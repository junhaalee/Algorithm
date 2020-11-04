import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

m,n,k = map(int, input().split())
graph = [[1]*n for _ in range(m)]

for _ in range(k):
    a,b,c,d = map(int,input().split())
    for i in range(b,d,1):
        for j in range(a,c,1):
            graph[i][j] = 0

dx,dy = [1,0,-1,0],[0,1,0,-1]

def dfs(count,x,y,graph):
    global dx,dy
    count += 1
    graph[x][y] = 0
    for i in range(4):
        tx,ty = x+dx[i],y+dy[i]
        if (0<=tx<m) and (0<=ty<n) and graph[tx][ty] == 1:
            count = dfs(count,tx,ty,graph)
    return count

answer = []
for x in range(len(graph)):
    for y in range(len(graph[0])):
        if graph[x][y]:
            answer.append(str(dfs(0,x,y,graph)))
answer = sorted(answer, key = lambda x : int(x))
print(len(answer))
print(' '.join(answer))