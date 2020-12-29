### 백준 - [18405](https://www.acmicpc.net/problem/18405)

### 풀이

* 다른 그래프 문제들과 다르게 graph 중심으로 풀어가는 것이 아니라 graph의 node들을 중심으로 풀어보았다.(사실 이렇게 안하면 시간초과가 뜬다)


```Python

#노드 중심
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




#graph 중심 - 시간초과
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
graph = [list(map(lambda x:[x,x],list(map(int,input().split())))) for _ in range(n)]
s,kx,ky = map(int, input().split())
dx,dy = [1,0,-1,0], [0,1,0,-1]

for _ in range(s):

    for x in range(n):
        for y in range(n):
            if graph[x][y][0]:
                for i in range(4):
                    tx,ty = x+dx[i],y+dy[i]
                    if (0<=tx<n) and (0<=ty<n) and graph[tx][ty][0] == 0:
                        if graph[tx][ty][1] == 0:
                            graph[tx][ty][1] = graph[x][y][0]
                        elif graph[tx][ty][1]>graph[x][y][0]:
                            graph[tx][ty][1] = graph[x][y][0]

    graph = [list(map(lambda x : [x[1],x[1]],graph[i])) for i in range(n)]

print(graph[kx-1][ky-1][0])
```

