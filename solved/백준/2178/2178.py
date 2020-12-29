h,w = map(int, input().split())

graph = []
for _ in range(h):
    graph.append(list(map(int,list(input()))))

visit = [[0,0]]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

count = 1
while(True):

    if [h-1,w-1] in visit:
        break

    temp = []
    for p in visit:
        for k in range(4):
            tx = p[0] + dx[k]
            ty = p[1] + dy[k]
            if tx>=0 and ty>=0 and tx<h and ty <w and graph[tx][ty]:
                temp.append([tx,ty])
                graph[tx][ty] = 0
    
    visit = temp
    count += 1

print(count)