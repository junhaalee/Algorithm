import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):

    k = int(input())

    if k == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,k)