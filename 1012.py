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

T = int(input())

for _ in range(T):

    X, Y, n = map(int, input().split())

    graph = [[0]*(Y+1) for _ in range(X+1)]

    for _ in range(n):
        link = list(map(int, input().split()))
        graph[link[0]][link[1]] = 1

    ans = []
    for x in range(X):
        for y in range(Y):
            if graph[x][y]:
                ans.append(len(detect(x,y,[])))

    print(len(ans))