### 백준 - [1753](https://www.acmicpc.net/problem/1753)

### 풀이

* 다익스트라 기본
* https://leetcode.com/problems/network-delay-time와 같은 문제

```Python

if node not in dist:
    dist[node] = time
    # 처음에는 새로운 노드가 graph안에 없을 경우를 생각 못했다
    if node in graph:
        for d,t in graph[node]:
            heapq.heappush(Q,(time+t,d))

```

