import sys
input = sys.stdin.readline

n,m = map(int, input().split())

ns = [input().strip() for _ in range(n)]
ms = [input().strip() for _ in range(m)]

ans = list(set(ns)&set(ms))

print(len(ans))

for a in sorted(ans):
    print(a)
