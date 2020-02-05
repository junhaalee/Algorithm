T = int(input())

test= []
for _ in range(T):
    test.append(int(input()))

nums = [1,1,1,2,2]

for i in range(5, max(test)):
    nums.append(nums[i-1] + nums[i-5])

for i in range(T):
    print(nums[test[i]-1])