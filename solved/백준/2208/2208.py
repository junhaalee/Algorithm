import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = [int(input()) for _ in range(n)]

best = -2001
current = 0

for i in range(m-1,len(nums)):
    current = max(current+nums[i], sum(nums[i-(m-1):i+1]))
    best = max(current, best)
    
print(best)