import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

result = [nums[0]]+[0 for _ in range(n-1)]

for i in range(1,n):
    for j in range(i):
        if nums[j] < nums[i]:
            result[i] = result[j]+nums[i]

print(max(result))
