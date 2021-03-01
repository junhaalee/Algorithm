### 백준 - [1937](https://www.acmicpc.net/problem/1937)

### 풀이

* DFS로 모든 node들을 탐색 - 시간초과
* DP를 이용하여 (0,0)부터 탐색 - 시간초과
* DP + (0,0)부터가 아닌 가장 큰 수(대나무의 양이 가장 많은)부터 max 값을 구하는 탐색 - OK

```Python
graph = []
order = []

for x in range(n):
    temp = list(map(int, input().split()))
    for y in range(n):
        order.append([temp[y],x,y])
    graph.append(temp)

# 대나무의 양이 가장 많은 위치부터 탐색할 수 있도록 정렬
order = sorted(order, key = lambda x : x[0], reverse=True)



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
                # dp에 저장된 값을 사용할 수 있다면, 저장된 값을 이용하여 탐색 끝
                if dp[nx][ny]:
                    result = max(result, length+dp[nx][ny])
                else:
                    stack.append([nx,ny,length+1])
    dp[x][y] = result
    return result
```

