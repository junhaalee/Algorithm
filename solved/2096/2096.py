import sys
input = sys.stdin.readline
mmax = [[0 for _ in range(3)] for _ in range(2)]
mmin = [[0 for _ in range(3)] for _ in range(2)]
for i in range(int(input())):

    nums = list(map(int, input().split()))

    mmax[1][0] = nums[0]+max(mmax[0][0],mmax[0][1])
    mmin[1][0] = nums[0]+min(mmin[0][0],mmin[0][1])
    mmax[1][1] = nums[1]+max(mmax[0][0],mmax[0][1],mmax[0][2])
    mmin[1][1] = nums[1]+min(mmin[0][0],mmin[0][1],mmin[0][2])
    mmax[1][2] = nums[2]+max(mmax[0][2],mmax[0][1])
    mmin[1][2] = nums[2]+min(mmin[0][2],mmin[0][1])

    mmax[0][0], mmax[0][1], mmax[0][2] = mmax[1][0], mmax[1][1], mmax[1][2]
    mmin[0][0], mmin[0][1], mmin[0][2] = mmin[1][0], mmin[1][1], mmin[1][2]

print(max(mmax[1]),min(mmin[1]))