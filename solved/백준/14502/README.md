### 백준 - [14502](https://www.acmicpc.net/problem/14502)

### 풀이

* 배열 복사 : deepcopy

```Python

def sol(graph, zc, n, m):
    
    # 배열 복사
    t_graph = copy.deepcopy(graph)
    
    for x,y in zc:
        t_graph[x][y] = 1
    
    dx, dy = [1,0,-1,0],[0,-1,0,1]
    queue = deque()

    for x in range(n):
        for y in range(m):
            if t_graph[x][y] == 2:
                queue.append([x,y])
                while queue:
                    tx,ty = queue.popleft()
                    for i in range(4):
                        nx,ny = tx+dx[i], ty+dy[i]
                        if (0<=nx<n) and (0<=ny<m) and t_graph[nx][ny] == 0:
                            t_graph[nx][ny] = 2
                            queue.append([nx,ny])
    
    count = 0
    for i in range(len(t_graph)):
        for k in range(len(t_graph[i])):
            if t_graph[i][k] == 0:
                count += 1
    
    return count

```