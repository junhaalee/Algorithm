### 백준  - [1932](https://www.acmicpc.net/problem/1932)

### 풀이

* dp라는 배열에 현재까지의 최적의 값을 구하는 형태로.

```Python
nums = [list(map(int, input().split())) for _ in range(int(input()))]

dp = [[nums[0][0]]]

for i in range(1, len(nums)):
    temp = []
    for k in range(len(nums[i])):
        if k == 0:
            temp.append(nums[i][k]+dp[i-1][0])
        elif k == len(nums[i])-1:
            temp.append(nums[i][k]+dp[i-1][-1])
        else:
            temp.append(nums[i][k]+max([dp[i-1][k], dp[i-1][k-1]]))
    dp.append(temp)

print(max(dp[-1]))
```

