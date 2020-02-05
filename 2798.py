from itertools import combinations, permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

case  = list(combinations(nums, 3))

ans = 0

for i in range(len(case)):
    if sum(case[i])-M == 0: 
        ans = sum(case[i])
        break
    elif sum(case[i])-M < 0 and sum(case[i])>ans:
        ans = sum(case[i])
        
print(ans)
