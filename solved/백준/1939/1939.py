import sys
from collections import deque,defaultdict
input = sys.stdin.readline

n,m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    x,y,v = map(int, input().split())
    graph[x].append([y,v])
    graph[y].append([x,v])

src, dist = map(int, input().split())

def dfs(graph, value, src, dist):

    visit[src] = 1
    stack = [src]

    while stack:

        node = stack.pop()

        if node == dist:
            return True

        for next,weight in graph[node]:
            if visit[next]==0 and weight >= value:
                stack.append(next)
                visit[next] = 1    
    return False


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
    if dfs(graph, mid, src, dist):
        min_v = mid + 1
    else:
        max_v = mid - 1

print(max_v)