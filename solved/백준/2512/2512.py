import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
st = int(input())

left,right = 1,max(nums)
ans = 0
while left<=right:

    mid = (left+right)//2

    temp = sum([num if mid>=num else mid for num in nums])

    if temp>st:
        right = mid-1
    else:
        left = mid+1
        ans = mid

print(ans)