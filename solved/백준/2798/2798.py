from itertools import combinations

n, k = map(int, input().split())

nums = list(map(int, input().split()))

case = list(combinations(nums, 3))

ans = 0
for c in case:
    if sum(c) <= k and sum(c) > ans:
        ans = sum(c)

print(ans)