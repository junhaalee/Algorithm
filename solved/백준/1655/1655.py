import sys
from heapq import heappop,heappush
input = sys.stdin.readline

left, right = [], []

for _ in range(int(input())):
    
    n = int(input())

    # 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 하므로.
    if len(left) == len(right):
        heappush(left, (-n,n))
    else:
        heappush(right, (n,n))

    if right and left[0][1] > right[0][1]:
        l = heappop(left)[1]
        r = heappop(right)[1]

        heappush(left, (-r,r))
        heappush(right, (l,l))

    print(left[0][1])