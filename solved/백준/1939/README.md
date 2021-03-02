### 백준 - [1939](https://www.acmicpc.net/problem/1939)

### 풀이

* 사소한 것으로 차이가 많이 난다
* visit = [] 해주고 visit.append(node) - 시간 초과
* visit = [0]*(n+1) 해주고 visit[node] = 1 - 통과

* 그래프 탐색과 이분 탐색을 이용해서 답을 구해야 한다.

```Python

def bfs(graph, value, src, dist):
    visit[src] = 1
    queue = deque([src])

    while queue:

        node = queue.popleft()

        if node == dist:
            return True

        for next, weight, in graph[node]:
            if not visit[next] and weight >= value:
                queue.append(next)
                visit[next] = 1

    return False

min_v, max_v = 1,1000000000

while min_v <= max_v:

    mid = (min_v+max_v)//2
    visit = [0]*(n+1)
    # mid라는 값으로 통과하는 것을 기준으로 이분 탐색
    if bfs(graph, mid, src, dist):
        min_v = mid + 1
    else:
        max_v = mid - 1

print(max_v)

```

