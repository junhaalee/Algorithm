### 백준  - [1149](https://www.acmicpc.net/problem/1149)

### 풀이

* dp라는 배열을 만들어서 현재 시점까지의 최적의 값을 저장하기.(습관을 들이면 굉장히 좋을듯)
* 이 문제는 '이번 단계에서 선택한 색깔과 이전 단계에서 선택한 색이 달라야 한다'라는 포인트

```Python
cost = [list(map(int, input().split())) for _ in range(int(input()))]

dp = [[0]*3 for _ in range(len(cost))]

dp[0] = cost[0]

for i in range(1, len(cost)):
    temp  = []

    dp[i][0] = cost[i][0]+min([dp[i-1][1], dp[i-1][2]])
    dp[i][1] = cost[i][1]+min([dp[i-1][0], dp[i-1][2]])
    dp[i][2] = cost[i][2]+min([dp[i-1][1], dp[i-1][0]])

print(min(dp[-1]))
```

