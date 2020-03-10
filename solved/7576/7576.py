w,h = map(int, input().split())

graph = []
one = []
for i in range(h):
    temp = list(map(int, input().split()))
    for k in range(len(temp)):
        if temp[k] == 1 : one.append([i,k])
    graph.append(temp)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

count = -1
while(True):

    if len(one) == 0:
        break

    temp = []
    while one:
        o = one.pop()
        for n in range(4):
            tx = o[0] + dx[n]
            ty = o[1] + dy[n]
            if tx>=0 and ty>=0 and tx<h and ty<w and graph[tx][ty] == 0:
                graph[tx][ty] = 1 
                temp.append([tx,ty])

    one = temp
    count += 1

for i in range(h):
    for k in range(w):
        if graph[i][k] == 0:
            count = -1
            break

print(count)