import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = defaultdict(list)

for _ in range(m):
    s,e,t = map(int, input().split())
    graph[s].append([e,t])

src, dst = map(int, input().split())


dist = defaultdict(int)

q = [(0,src)]

while q:

    time, node = heapq.heappop(q)

    if node not in dist:
        dist[node] = time
        for e,t in graph[node]:
            heapq.heappush(q,(t+time,e))

print(dist[dst])
