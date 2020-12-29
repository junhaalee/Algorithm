import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

ans = []

data = dict(Counter(ns))

for mm in ms:
    try:
        ans.append(data[mm])
    except:
        ans.append(0)

print(' '.join(list(map(str,ans))))