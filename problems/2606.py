n = int(input())

graph = [[0]*(n+1) for _ in range(n+1) ]

for _ in range(int(input())):
    link = list(map(int, input().split()))
    graph[link[0]][link[1]] = 1
    graph[link[1]][link[0]] = 1    

def bfs():

    current = 1
    queue = [current]
    visit = [current]

    while(queue):
        current = queue.pop(0)
        for next in range(len(graph[current])):
            if graph[current][next] and next not in visit:
                queue += [next]
                visit += [next]
   
    return visit

print(len(bfs())-1)