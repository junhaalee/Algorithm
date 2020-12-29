import sys
input = sys.stdin.readline

while(True):

    nums = list(map(int, input().split()))


    if len(nums) == 1 and nums[0] == 0:
        break
    else:
        nums = list(map(int, '9 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 999999999 1000000000 1000000000'.split(' ')))

        ans = 0
        temp = nums[0]
        count = 1

        i = 1
        while(i<=len(nums)):
            if i == len(nums):
                ans = temp*count if temp*count >= ans else ans
            else:
                if temp <= nums[i]:
                    if temp*(count+1) > nums[i]:
                        count += 1
                    else:
                        temp = nums[i]
                        count = 1
                else:
                    ans = temp*count if temp*count >= ans else ans
                    temp = nums[i]
                    count = 1
            i += 1
        print(ans)