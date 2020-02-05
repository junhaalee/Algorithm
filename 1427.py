nums = list(input())

int_nums = list(map(int, nums))
int_nums.sort(reverse=True)

ans = ''

for i in range(len(int_nums)):
    ans += str(int_nums[i])
print(ans)