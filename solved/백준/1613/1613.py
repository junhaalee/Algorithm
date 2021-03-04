import sys
input = sys.stdin.readline

n,k = map(int, input().split())

graph = [[0]*n for _ in range(n)]

for _ in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1

question = [list(map(int, input().split())) for _ in range(int(input()))]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for a,b in question:
    if graph[a-1][b-1]:
        print(-1)
    elif graph[b-1][a-1]:
        print(1)
    elif not graph[a-1][b-1]:
        print(0)

