n = int(input())

graph = [[0]*(n+1) for _ in range]


house = []
for _ in range(int(input())):
    house += [list(map(int, list(input())))]


print(graph)





def dfs(current, graph, visit):
    visit.append(current)

    for next in range(len(graph[current])):
        if graph[current][next] and next not in visit:
            visit = dfs(next,graph,visit)
    return visit

answer = []