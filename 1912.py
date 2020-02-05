n = int(input())
nums = [0]+list(map(int, input().split()))
result = -1001
temp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    temp[i] = max(nums[i], nums[i]+temp[i-1])
    result = max(result, temp[i])
print(result)