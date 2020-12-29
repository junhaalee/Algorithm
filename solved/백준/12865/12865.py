n,k = map(int, input().split())

bags = sorted([list(map(int, input().split())) for _ in range(n)], key = (lambda x : x[0]))

dp = [0]*(k+1)

for i in range(len(bags)):
    for j in range(k,0,-1):
        if bags[i][0] <= j:
            dp[j] = max([dp[j], bags[i][1]+dp[j-bags[i][0]]])

print(dp[-1])