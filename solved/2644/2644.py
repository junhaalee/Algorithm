import sys 
input = sys.stdin.readline

n = int(input())

start, end = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(int(input())):
    link = list(map(int,input().split()))
    graph[link[0]][link[1]] = 1
    graph[link[1]][link[0]] = 1


def dfs(visit,graph,current):
    visit.append(current)
    for next in range(len(graph[current])):
        if graph[current][next] and next not in visit:
            visit = dfs(visit,graph,next)
    return visit

check = dfs([],graph,start)

if end in check:
    count = 0
    visit = [start]
    while(True):

        if end in visit:
            break

        temp = []

        for start in visit:
            for i in range(len(graph[start])):
                if graph[start][i] == 1:
                    temp.append(i)
        visit = temp
        count += 1

    print(count)
else:
    print(-1)