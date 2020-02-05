n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int,list(input()))))

def detect(x,y,visit):

    if graph[x][y] and [x,y] not in visit:
        if x >= 0 and y >= 0:
            visit.append([x,y])
            graph[x][y] = 0
            try:
                if graph[x+1][y] :
                    visit = detect(x+1,y,visit)
            except:pass

            try:        
                if graph[x][y+1] :
                    visit = detect(x,y+1,visit)  
            except:pass  
    
            if graph[x][y-1]:
                visit = detect(x,y-1,visit)
            if graph[x-1][y]:
                visit = detect(x-1,y,visit)

    return visit

ans = []
for x in range(n):
    for y in range(n):
        if graph[x][y]:
            ans.append(len(detect(x,y,[])))

print(len(ans))
for a in sorted(ans):
    print(a)