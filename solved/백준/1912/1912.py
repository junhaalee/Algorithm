import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

best = -sys.maxsize
current = 0
for num in nums:
    current = max(num, current+num)
    best = max(best, current)

print(best)