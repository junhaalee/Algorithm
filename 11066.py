def div(nums):
    temp = []
    for ind in range(1,len(nums),2):
        temp.append(nums[ind]+nums[ind-1])
    return temp

T = int(input())

for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))

    nums = [1,2,3,4,5,6]
    total = 0

    while(True):

        if len(nums) == 1:
            break

        if len(nums)%2 == 0:
            total += sum(nums)
            nums = div(nums)
        
        else:
            total += sum(nums) - max(nums)
            max_num = max(nums)
            del nums[nums.index(max(nums))]
            nums = div(nums)
            nums.append(max_num)

    print(total)
