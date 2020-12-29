from collections import deque

n,m = map(int, input().split())
nums = deque(list(map(int, input().split())))
arr = deque([x+1 for x in range(n)])

count = 0
while(nums):

    if arr[0] == nums[0]:
        nums.popleft()
        arr.popleft()
    else:
        k = arr.index(nums[0])
        if k <= len(arr)//2:
            count += k
            for _ in range(k):
                arr.rotate(-1)
        else:
            count += len(arr)-k
            for _ in range(len(arr)-k):
                arr.rotate(1)

print(count)