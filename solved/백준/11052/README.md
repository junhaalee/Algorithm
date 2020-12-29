### 백준  - [11052](https://www.acmicpc.net/problem/11052)

### 풀이

* .

```Python
for i in range(1,len(price)):
    temp = [price[i]]
    for k in range(i//2+1):
        temp.append(dp[i-k-1]+dp[k])
    dp[i] = max(temp)
```

