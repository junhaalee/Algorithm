from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
src = int(input())

graph = defaultdict(list)

for _ in range(m):
    u,v,w = map(int, input().split())
    graph[u].append([v,w])

Q = [(0,src)]
dist = defaultdict(int)

while Q:

    time, node = heapq.heappop(Q)

    if node not in dist:
        dist[node] = time
        if node in graph:
            for d,t in graph[node]:
                heapq.heappush(Q,(time+t,d))

for i in range(1,n+1):
    print(dist[i]) if i in dist else print('INF')