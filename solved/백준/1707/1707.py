from collections import defaultdict,deque
import sys
input = sys.stdin.readline

def sol(graph, v,e):

    check = [-1]*(v+1)
    queue = deque()

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
        
n = int(input())

for _ in range(n):

    v,e = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(e):
        s,d = map(int, input().split())
        graph[s].append(d)
        graph[d].append(s)

    print(sol(graph,v,e))