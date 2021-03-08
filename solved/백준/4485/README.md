### 백준 - [4485](https://www.acmicpc.net/problem/4485)

### 풀이

* 다익스트라

```Python

while queue:

    value, x, y = heapq.heappop(queue)

    if [x,y] == [n-1,n-1]:
        break

    for i in range(4):
        tx,ty = x+dx[i],y+dy[i]

        # 아직 방문하지 않은 곳에 대해서
        # 값 update 해주기
        if (0<=tx<n) and (0<=ty<n) and visit[tx][ty] == 0:
            dp[tx][ty] = value+graph[tx][ty]
            heapq.heappush(queue, [dp[tx][ty],tx,ty])
            visit[tx][ty] = 1

```

