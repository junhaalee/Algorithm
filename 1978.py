n = int(input())

nums = list(map(int, input().split()))

def sol(n):
    div = 0
    for i in range(1, n+1):
        if n%i == 0 :
            div += 1
    if div == 2:
        return True
    else:
        return False

ans = 0

for num in nums:
    if sol(num) == True: ans += 1

print(ans)