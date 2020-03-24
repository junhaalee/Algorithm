import sys
input = sys.stdin.readline

n,m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1,0,1]
dy = [0,1,1]

for x in range(n):
    for y in range(m):
        if x+y:
            temp = []
            for i in range(3):
                tx = x - dx[i]
                ty = y - dy[i]
                if tx >= 0 and ty >= 0 and tx < n and ty < m:
                    temp.append(graph[tx][ty])
            graph[x][y] += max(temp)
            
print(graph[n-1][m-1])