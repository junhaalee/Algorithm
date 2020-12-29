import heapq
import sys
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    k = int(input())

    if k == 0:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,-k)