### 프로그래머스 - [합승택시요금](https://programmers.co.kr/learn/courses/30/lessons/72413)

### 풀이

* 다익스트라
* 플로이드-와샬

```Python
# 1. 다익스트라 이용
    # 다익스트라 표준
    def dik(src, dest):
        
        queue = [[0,src]]
        dik = [sys.maxsize]*(n+1)
        dik[src] = 0

        while queue:
        
            cost, current = heapq.heappop(queue)
            
            if dik[current] < cost:
                continue

            for next, ncost in graph[current]:
                ncost += cost
                if dik[next] > ncost:
                    dik[next] = ncost
                    heapq.heappush(queue, [ncost,next])
        
        return dik[dest]

# 2. 플로이드-와샬
    # 3중 for문으로 구현
    # i를 거쳐가는 path에 대한 weight 비교
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if graph[j][k] > graph[j][i]+graph[i][k]:
                    graph[j][k] = graph[j][i]+graph[i][k]
                    
    for i in range(1, n+1):
        answer = min(answer, graph[s][i]+graph[i][a]+graph[i][b])
        
```

