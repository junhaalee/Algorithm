import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n,m = 6,4

graph = []

for _ in range(n):
    graph.append(list(map(int, list(input())[:-1])))




graph = [[0, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]
visit = [[0]*m for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]



count = 0
check = 0


while(True):

    if [n-1,m-1] in temp:
        break


    ch = True
    if check:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if (0<=tx<n) and (0<=ty<m) and graph[tx][ty] == 0 and visit[tx][ty] == 0:
                ch = False
                break
        
        if ch:
            print(-1)
            break
        else:
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if (0<=tx<n) and (0<=ty<m) and graph[tx][ty] == 0 and visit[tx][ty] == 0:













def dfs(x,y,check,count):
    global dx,dy,visit
    print(x,y,count)
    count += 1
    visit[x][y] = 1
    ch = True
    if check:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if (0<=tx<n) and (0<=ty<m) and graph[tx][ty] == 0 and visit[tx][ty] == 0:
                ch = False
                break

        if ch:
            return -1
        else:
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if (0<=tx<n) and (0<=ty<m) and graph[tx][ty] == 0 and visit[tx][ty] == 0:
                    count = dfs(tx,ty,1,count)

    else:
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if (0<=tx<n) and (0<=ty<m) and graph[tx][ty] == 0 and visit[tx][ty] == 0:
                count = dfs(tx,ty,0,count)
            elif (0<=tx<n) and (0<=ty<m) and graph[tx][ty] == 1 and visit[tx][ty] == 0:
                cout = dfs(tx,ty,1,count)
    return count
