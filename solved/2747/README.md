### 백준  - [2747](https://www.acmicpc.net/problem/2747)

### 풀이

* dp 배열을 이용한 피보나치

```Python
n = int(input())
if n <= 2:
    print(1)
else:
    dp = [0,1,1] + [0 for _ in range(n-2)]

    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    print(dp[-1])
```

