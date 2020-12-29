n, count = int(input()), 0
nums = [64,32,16,8,4,2,1]
ind = 0
while(n):

    if nums[ind] <= n:
        count += n//nums[ind]
        n %= nums[ind]
    ind += 1

print(count)