### 백준  - [2579](https://www.acmicpc.net/problem/2579)

### 풀이

* 마지막 계단을 반드시 밟아야 한다는 조건 때문에, 역순으로 풀어나가려고 했지만 아래와 같은 방법으로도 마지막 계단을 반드시 밟게할 수 있다.

```Python
stairs = [int(input()) for _ in range(int(input()))]

dp = [stairs[0], stairs[0]+stairs[1],max([stairs[2]+stairs[0],stairs[2]+stairs[1]])]

for i in range(3, len(stairs)):
    dp.append(max([stairs[i]+stairs[i-1]+dp[i-3],stairs[i]+dp[i-2]]))

print(dp[-1])
```

