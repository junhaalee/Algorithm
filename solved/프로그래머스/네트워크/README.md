### 백준  - [네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3)

### 풀이

* 백준의 11724번 문제와 비슷한 문제

```Python
def dfs(current, visit, graph):

    visit.append(current)

    for next in range(len(graph[current])):
        if graph[current][next] and next not in visit:
            visit = dfs(next,visit,graph)
    
    return visit
```

