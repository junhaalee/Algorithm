size, st = input().split()
nums = input().split(' ')

size = int(size)
st = int(st)

ans = ''

for i in range(len(nums)):
    if int(nums[i])<st:
        ans += nums[i]+' '

print(ans)
    