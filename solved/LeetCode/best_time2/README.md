### LeetCode - [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

### 풀이

* 그리디 : 각 단계마다 최적해 찾기
* DP : 하위 문제에 대한 최적의 솔루션을 찾은 다음, 이 결과들을 결합

```Python

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0  

        # 각 단계마다 팔 수 있으면 팔아버리기
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit += (prices[i]-prices[i-1])
        
        return profit

# 2. Pythonic
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max((prices[i+1]-prices[i]),0) for i in range(len(prices)-1))

```