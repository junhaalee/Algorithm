n = int(input())
nums = list(map(int, input().split()))

num = [1 for _ in range(n)]

for i in range(n):
    count = 0
    for j in range(i):
        if nums[j] < nums[i]:
            num[i] = max(num[i], num[j]+1)

print(max(num))