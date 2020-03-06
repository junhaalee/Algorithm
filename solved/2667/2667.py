n = int(input())

house = []
for _ in range(n):
    house.append(list(map(int, list(input()))))

def dfs(x,y,graph,visit,n):
    if x>=0 and y>=0 and x<n and y <n and graph[x][y] and [x,y] not in visit:
        visit.append([x,y])
        graph[x][y] = 0
        if x+1 <= n:
            visit = dfs(x+1,y,graph,visit,n) 
        if y+1 <= n:
            visit = dfs(x,y+1,graph,visit,n) 
        visit = dfs(x-1,y,graph,visit,n) 
        visit = dfs(x,y-1,graph,visit,n)
    return visit

answer = []
for i in range(n):
    for k in range(n):
        if house[i][k]:
            answer.append(len(dfs(i,k,house,[],n)))
answer.sort()
print(len(answer))
for a in answer:
    print(a)
