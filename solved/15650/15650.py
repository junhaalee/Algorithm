from itertools import combinations

n,m = map(int, input().split())
nums = [x+1 for x in range(n)]

if m == 1:
    for num in nums:
        print(num)
else:   
    ans = list(combinations(nums,m))
    for a in ans:
        print(' '.join(map(str, list(a))))