### 백준  - [9205](https://www.acmicpc.net/problem/9205)

### 풀이

* 플로이드 알고리즘 : 거쳐가는 정점을 기준으로 target까지의 최단 거리를 구하는 알고리즘.
* https://m.blog.naver.com/PostView.nhn?blogId=ndb796&logNo=221234427842&proxyReferer=https%3A%2F%2Fwww.google.com%2F


```Python
def bfs(x,y):
    que, current = deque(),[]
    que.append([x,y,20])
    current.append([x,y,20])

    while que:
        x,y,b = que.popleft()
        if x == tx and y == tx:
            print('happy')
            return
        for nx, ny in D:
            if [nx, ny, 20] not in current:
                l = abs(ny-y) + abs(nx-x)
                if b*50 >= l:
                    que.append([nx,ny,20])
                    current.append([nx,ny,20])
    print('sad')
    return
```

