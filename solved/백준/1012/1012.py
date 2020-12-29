import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx,dy = [1,0,-1,0],[0,1,0,-1]

def dfs(count,x,y):
    global dx,dy,graph
    count += 1
    graph[x][y] = 0
    for i in range(4):
        tx,ty = x + dx[i],y + dy[i]    
        if (0<=tx<w) and (0<=ty<h) and graph[tx][ty]:
            count = dfs(count,tx,ty)
    return count

answer = []

for _ in range(int(input())):

    w,h,n = map(int, input().split())
    graph = [[0]*h for _ in range(w)]

    for _ in range(n):
        x,y = map(int,input().split())
        graph[x][y] = 1

    count = 0
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            if graph[x][y]:
                check = dfs(0,x,y)
                count += 1
    
    answer.append(count)

for a in answer:
    print(a)
            
