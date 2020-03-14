import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
temp = [0,nums[0]]

for i in range(1,n):
    if nums[i] < temp[-1] and nums[i] > temp[-2]:
        temp[-1] = nums[i]
    elif nums[i] > temp[-1]:
        temp.append(nums[i])
print(len(temp)-1)
