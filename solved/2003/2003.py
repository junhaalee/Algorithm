import sys
input = sys.stdin.readline

a,b = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

s,e = 0,0
while s<=e and e<=len(nums):
    if sum(nums[s:e]) < b:
        e += 1
    elif sum(nums[s:e]) > b:
        s += 1
    else:
        ans += 1
        s += 1
        e = s

print(ans)