n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))

ans = []

for i in range(len(nums)):
    if nums[i] != 0:
        ans.append(nums[i])
    else :
        ans.pop()

print(sum(ans))