for _ in range(int(input())):
    
    w,h,l = map(int, input().split())

    graph = [[0]*h for _ in range(w)]

    for _ in range(l):
        link = list(map(int, input().split()))
        graph[link[0]][link[1]] = 1

    def dfs(x,y,graph,visit):
        if x>=0 and y>=0 and x < w and y < h and graph[x][y] and [x,y] not in visit :
            visit.append([x,y])
            graph[x][y] = 0
            visit = dfs(x+1,y,graph,visit)
            visit = dfs(x,y+1,graph,visit)
            visit = dfs(x-1,y,graph,visit)
            visit = dfs(x,y-1,graph,visit)
        return visit

    answer = []
    for x in range(w):
        for y in range(h):
            if graph[x][y]:
                answer.append(dfs(x,y,graph,[]))

    print(len(answer))