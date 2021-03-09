import sys
input = sys.stdin.readline

n,s = map(int, input().split())

nums = list(map(int, input().split()))

if sum(nums) < s:
    print(0)
else:
    left, right = 0,0
    sum = nums[0]
    ans = sys.maxsize

    while right < len(nums):

        if sum < s:
            right += 1
            if right < len(nums):
                sum += nums[right]
            
        else:
            ans = min(ans, right-left+1)
            sum -= nums[left]
            left += 1

    print(ans)