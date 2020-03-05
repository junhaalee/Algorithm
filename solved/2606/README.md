### 백준  - [2606](https://www.acmicpc.net/problem/2606)

### 풀이

* 문제를 잘 읽자. 1번 컴퓨터를 통해 감염되는 컴퓨터를 구하는 문제니깐, visit에서 1번 컴퓨터는 빼야지.
* BFS와 DFS를 그대로 가져다 쓰면 되는 아주 쉬운 그래프 문제였다.

```Python
def dfs(current, graph, visit):
    visit.append(current)
    for next in range(len(graph[current])):
        if graph[current][next] and next not in visit:
            visit = dfs(next, graph, visit)
    return visit

print(len(dfs(1,graph,[]))-1)
```

