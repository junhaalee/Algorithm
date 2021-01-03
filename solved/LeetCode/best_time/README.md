### LeetCode - [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

### 풀이

* 카데인 알고리즘(Kadane's Algorithm)
* 배열의 최대 부분 합을 O(n)의 시간복잡도로 구하는 알고리즘 - DP의 일종
* https://velog.io/@w-beom/%EC%B9%B4%EB%8D%B0%EC%9D%B8-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%B5%9C%EB%8C%80-%EB%B6%80%EB%B6%84%ED%95%A9

```Python

# 1. 나의 풀이 O(n^2) - 5044ms / 15.4MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)-1):
            ans = max(ans,max(prices[i+1:])-prices[i])
        return ans


# 2. 카데인 알고리즘 O(n) - 64ms / 15.1
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price-min_price)
        
        return profit
```

### 관련 문제
* 백준 1912
* 백준 2208