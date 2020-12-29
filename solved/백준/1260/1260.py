n, e, s = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(e):
    link = list(map(int, input().split()))
    graph[link[0]][link[1]] = 1
    graph[link[1]][link[0]] = 1


def dfs(current, graph, visit):
    visit.append(current)

    for next in range(len(graph[current])):
        if graph[current][next] and next not in visit:
            visit = dfs(next, graph, visit)
    
    return visit

def bfs(current):
    
    queue = [current]
    visit = [current]

    while(queue):
        current = queue.pop(0)

        for next in range(len(graph[current])):
            if graph[current][next] and next not in visit:
                visit += [next]
                queue += [next]
    
    return visit


print(' '.join(map(str,dfs(s,graph,[]))))
print(' '.join(map(str,bfs(s))))