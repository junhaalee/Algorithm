### 백준  - [11724](https://www.acmicpc.net/problem/11724)

### 풀이

* 더욱 빠른 DFS 만들기

```Python
### 내가 자주 사용하던 DFS

def dfs(current, visit, graph):
	visit.append(current)

	for next in range(len(graph[current])):
		if graph[current][next] and next not in visit:
			visit = dfs(next, visit, graph)

	return visit



### 속도를 더욱 향상 시켜준 DFS
def dfs(current):
    global graph, visit
    visit[current] = 1

    for next in range(len(graph[current])):
        if graph[current][next] and visit[next] == 0:
            visit = dfs(next)
            
    return visit
```

* visit이라는 [0 for _ in range(n+1)]이라는 배열을 만들어놓고, 방문하였으면 visit[current] = 1로 만들어 준다.