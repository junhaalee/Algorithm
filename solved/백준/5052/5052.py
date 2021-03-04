import sys
input = sys.stdin.readline

def sol(nums):

    for i in range(len(nums)-1):
        if nums[i+1].startswith(nums[i]):
            return False
    return True
            
for _ in range(int(input())):

    nums = sorted([input().strip() for _ in range(int(input()))])
    
    if sol(nums):
        print('YES')    
    else:
        print('NO')
