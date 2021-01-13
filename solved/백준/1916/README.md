### 백준 - [1916](https://www.acmicpc.net/problem/1916)

### 풀이

* 입력받는 데이터가 많을 때, sys.stdin.readline의 효과는 엄청남.
* sys.stdin.readline 있으면 통과, 없으면 시간초과

```Python
input = sys.stdin.readline

# 다익스트라 알고리즘은 1753번과 동일
while q:

    time, node = heapq.heappop(q)

    if node not in dist:
        dist[node] = time
        for e,t in graph[node]:
            heapq.heappush(q,(t+time,e))

print(dist[dst])
```