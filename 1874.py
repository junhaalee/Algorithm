n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

temp = [0]

ans = []

ind = 0

while(True):

    if ind >= n+1:
        print('NO')
        break

    if len(nums) == 0:
        for i in range(len(ans)):
            print(ans[i])
        break

    if temp[-1] != nums[0] :
        ind += 1
        temp.append(ind)
        ans.append('+')

    else:
        temp.pop()
        del nums[0]
        ans.append('-')