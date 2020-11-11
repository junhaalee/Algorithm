import sys
input = sys.stdin.readline

n,k = map(int, input().split())
index = [[] for _ in range(k)]
graph = [list(map(int,input().split())) for _ in range(n)]
s,kx,ky = map(int, input().split())
dx,dy = [1,0,-1,0], [0,1,0,-1]

for x in range(n):
    for y in range(n):
        if graph[x][y]:
            index[graph[x][y]-1].append([x,y])

for _ in range(s):

    for ind in index:

        if ind:
            temp = []
            while ind:
                cu = ind.pop()
                x,y = cu[0],cu[1]
                for i in range(4):
                    tx,ty = x+dx[i],y+dy[i]
                    if (0<=tx<n) and (0<=ty<n) and graph[tx][ty] == 0:
                        graph[tx][ty] = graph[x][y]
                        temp.append([tx,ty])
            
            index[graph[x][y]-1] = temp

print(graph[kx-1][ky-1])