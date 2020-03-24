### 백준  - [10026](https://www.acmicpc.net/problem/10026)

### 풀이

* 재귀문제에서는 sys.setrecursionlimit() 설정하도록 하자. 단, PyPy에서는 설정 불가능. 

```Python
def dfs(graph,visit,current,check_graph):
    
    x,y = current[0],current[1]
    visit.append(current)
    
    if check_graph[x][y]:
        check_graph[x][y] = 0
        for i in range(4):
            tx = x+dx[i]
            ty = y+dy[i]

            if tx >= 0 and ty >= 0 and tx < n and ty < n and graph[tx][ty] != 0 and graph[x][y] == graph[tx][ty] and check_graph[tx][ty]:
                next = [tx,ty]
                dfs(graph,visit,next,check_graph)
        
        return visit
    else:
        return 0
```

* 다른 DFS 문제랑 비슷한 부분이 많았지만, 한번 들렸던 노드에 대해서 체크해주기 위해 따로 체크하는 배열을 만들어서 체크해주었다.