import sys
input = sys.stdin.readline
n = int(input())

graph = []
order = []

for x in range(n):
    temp = list(map(int, input().split()))
    for y in range(n):
        order.append([temp[y],x,y])
    graph.append(temp)

order = sorted(order, key = lambda x : x[0], reverse=True)

dp = [[0]*n for _ in range(n)]
dx,dy = [1,0,-1,0],[0,1,0,-1]

def dfs(x,y):
    
    global dx,dy,dp
    
    stack = [[x,y,1]]
    result = 1
    while stack:

        tx,ty,length = stack.pop()
        value = graph[tx][ty]
        result = max(result, length)

        for i in range(4):
            nx,ny = tx+dx[i], ty+dy[i]
            if (0<=nx<n) and (0<=ny<n) and graph[nx][ny] > value:
                if dp[nx][ny] != 0:
                    result = max(result, length+dp[nx][ny])
                else:
                    stack.append([nx,ny,length+1])
    dp[x][y] = result
    return result

result = 1

for _,x,y in order:
    result = max(result, dfs(x,y))

print(result)