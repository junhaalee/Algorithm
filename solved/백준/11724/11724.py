import sys
input = sys.stdin.readline
n,m = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    link = list(map(int, input().split()))
    graph[link[0]][link[1]] = 1
    graph[link[1]][link[0]] = 1

def dfs(current):
    global graph, visit
    visit[current] = 1

    for next in range(len(graph[current])):
        if graph[current][next] and visit[next] == 0:
            visit = dfs(next)
            
    return visit

ans = []
for i in range(1,n+1):
    visit = [0 for _ in range(n+1)]
    temp = dfs(i)
    if temp not in ans:
        ans.append(temp)

print(len(ans))