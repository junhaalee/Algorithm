w,h = map(int, input().split())

graph = []
for _ in range(h):
    graph.append(list(map(int, input().split())))

# graph = [[1, -1, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0], [0, 0, 0, 0, -1, 1]]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def check(graph):
    num = 0
    for i in range(h):
        for k in range(w):
            if graph[i][k] == 0 : num += 1

    return num

count = 0
while(True):

    bch = check(graph)

    if bch == 0:
        break

    temp = []
    for i in range(h):
        for k in range(w):
            if graph[i][k] == 1:
                for n in range(4):
                    tx = i + dx[n]
                    ty = k + dy[n]
                    if tx>=0 and ty>=0 and tx<h and ty<w and graph[tx][ty] == 0 : temp.append([tx,ty])
    
    for t in temp:
        graph[t[0]][t[1]] = 1
    ach = check(graph)

    if ach == bch:
        count = -1
        break
                    
    count += 1

print(count)