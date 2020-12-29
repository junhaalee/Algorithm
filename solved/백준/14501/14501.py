sch = [list(map(int, input().split())) for _ in range(int(input()))]

sch = [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]]

dp = [0]*(len(sch)+1)

for i in range(len(sch),-1,-1):
    dp[i] = max(dp[i],sch[i-1][1]+dp[i-1+sch[i-1][0]])


