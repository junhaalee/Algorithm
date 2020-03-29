import sys
input = sys.stdin.readline

n = int(input())
price = list(map(int, input().split()))

dp = [price[0]]+[0 for _ in range(n-1)]

for i in range(1,len(price)):
    temp = [price[i]]
    for k in range(i//2+1):
        temp.append(dp[i-k-1]+dp[k])
    dp[i] = max(temp)

print(dp[-1])
