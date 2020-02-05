# 방법 1 - Brute Force
# from itertools import permutations

# num = list(input())

# nums = list(permutations(num,len(num)))

# ans = 0

# for i in range(len(nums)):
#     temp = ''
#     for j in range(len(nums[i])):
#         temp += nums[i][j]
#     if int(temp)%30 == 0 and int(temp)>ans:
#         ans = int(temp)

# if ans == 0:
#     print(-1)
# else:
#     print(ans)


# 방법 2 - Greedy
nums = list(input())

nums = sorted(nums, reverse = True)

if nums[-1] != '0' or sum(map(int,nums))%3 != 0:
    print(-1)

else:
    ans = ''
    for i in range(len(nums)):
        ans += nums[i]
    print(ans)