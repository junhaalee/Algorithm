stairs = [int(input()) for _ in range(int(input()))]

dp = [stairs[0], stairs[0]+stairs[1],max([stairs[2]+stairs[0],stairs[2]+stairs[1]])]

for i in range(3, len(stairs)):
    dp.append(max([stairs[i]+stairs[i-1]+dp[i-3],stairs[i]+dp[i-2]]))

print(dp[-1])