n,m = map(int, input().split())

graph = [list(map(int, list(input()))) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
one = []
for i in range(n):
    for k in range(m):
        if graph[i][k] == 1:
            count = 0
            for j in range(4):
                tx = i + dx[j]
                ty = k + dy[j]
                if tx >= 0 and ty >= 0 and tx < n and ty < m and graph[tx][ty] == 0:
                    count += 1
            if count != 0:
                one.append([i,k])

def bfs(graph,n,m):

    current = [[0,0]]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    count = 1
    while(True):

        if graph[n-1][m-1] != 0:
            break

        temp = []
        check = 0
        for c in current:
            for k in range(4):
                tx = c[0]+dx[k]
                ty = c[1]+dy[k]
                if tx >=0 and ty >=0 and tx < n and ty < m and graph[tx][ty] == 0:
                    graph[tx][ty] = count
                    temp.append([tx,ty])
                else:
                    check += 1
        count += 1
        current = temp

        if check == 4:
            graph[n-1][m-1] = -2
            break

    return graph[n-1][m-1]+1

ans = []

for o in one:
    t_graph = graph
    t_graph[o[0]][o[1]] = 0
    ans.append(bfs(t_graph,n,m))

print(len(ans))