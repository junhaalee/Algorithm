### 백준 - [1707](https://www.acmicpc.net/problem/1707)

### 풀이

* 이분 그래프 : 그래프의 모든 정점이 두 그룹으로 나눠지고 서로 다른 그룹의 정점이 간선으로 연결된 그래프

```Python
def sol(graph, v,e):

    # 노드 확인
    check = [-1]*(v+1)
    # BFS
    queue = deque()

    # 모든 노드들이 연결되어 있다는 보장이 없으므로 
    # 모든 노드들을 확인해줘야 함.
    for node in range(1,v+1):

        if check[node] == -1:
            check[node] = True
            queue.append([node, True])
            while queue:
                no, ch = queue.popleft()
                for neighbor in graph[no]:
                    if check[neighbor] == -1:
                        check[neighbor] = not(ch)
                        queue.append([neighbor, not(ch)])
                    else:
                        if check[neighbor] == ch:
                            return 'NO'
    return 'YES'
```

