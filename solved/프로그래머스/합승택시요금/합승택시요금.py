# 다익스트라
from collections import defaultdict
import heapq
import sys
def solution(n, s, a, b, fares):
    
    def dik(src, dest):
        
        queue = [[0,src]]
        dik = [sys.maxsize]*(n+1)
        dik[src] = 0

        while queue:
            cost, current = heapq.heappop(queue)
            
            if dik[current] < cost:
                continue

            for next, ncost in graph[current]:
                ncost += cost
                if dik[next] > ncost:
                    dik[next] = ncost
                    heapq.heappush(queue, [ncost,next])
        
        return dik[dest]

    graph = defaultdict(list)
    
    for start, end, cost in fares:
        graph[start].append([end, cost])
        graph[end].append([start, cost])

    cost = sys.maxsize
    
    for i in range(1, n+1):
        cost = min(cost, dik(s,i)+dik(i,a)+dik(i,b))    

    return cost


# 플로이드 와샬
import sys
def solution(n, s, a, b, fares):
    m = sys.maxsize
    graph = [[m]*(n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        graph[i][i] = 0

    for start, end, cost in fares:
        graph[start][end] = cost
        graph[end][start] = cost

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if graph[j][k] > graph[j][i]+graph[i][k]:
                    graph[j][k] = graph[j][i]+graph[i][k]

    answer = sys.maxsize

    for i in range(1, n+1):
        answer = min(answer, graph[s][i]+graph[i][a]+graph[i][b])
        
    return answer