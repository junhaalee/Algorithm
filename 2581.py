s = int(input())
f = int(input())

def sol(n):
    div = 0
    for i in range(1, n+1):
        if n%i == 0 :
            div += 1
    if div == 2:
        return True
    else:
        return False

nums = []

for i in range(s, f+1):
    if sol(i) == True: nums.append(i)

if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))