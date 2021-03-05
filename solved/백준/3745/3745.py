import sys
import bisect
input = sys.stdin.readline
result = []

def sol(nums):
    global result

    index, current = 0, 100001
    answer = 1

    for next_index, next in enumerate(nums):
        if current >= next:
            index = next_index
        answer = max(answer, next_index-index+1)
        current = next
        
    result.append(answer)

def sol2(nums):
    global result

    dp = [0]

    for num in nums:
        if num > dp[-1]:
            dp.append(num)
        else:
            dp[bisect.bisect_left(dp, num)] = num
    
    result.append(len(dp)-1)
        
while True:
    try:
        n = int(input())
        nums = list(map(int ,input().split()))
        sol2(nums)
    except:
        break

for r in result:
    print(r)