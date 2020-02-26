### 백준  - [2156](https://www.acmicpc.net/problem/2156)

### 풀이

* 와인의 개수가 1개일 때
* dp[k]를 정할때, dp[k-1]도 비교 대상에 추가해줘야 함.

```Python
wine = [0]+[int(input()) for _ in range(int(input()))]

if len(wine) > 2:
    dp = [0,wine[1], wine[1]+wine[2]]+[0]*(len(wine)-3)
else:
    dp = [0,wine[1]]

for k in range(3,len(wine)):

    dp[k] = max([ dp[k-2]+wine[k], dp[k-3]+wine[k-1]+wine[k], dp[k-1]  ])

print(max(dp))
```

