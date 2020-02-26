### 백준  - [12865](https://www.acmicpc.net/problem/12865)

### 풀이

* 냅색
* DP는 식을 잘짜면 된다, dp 배열을 만드는 습관을 들이자.

```Python

dp[j] = max([dp[j], bags[i][1]+dp[j-bags[i][0]]])

```

