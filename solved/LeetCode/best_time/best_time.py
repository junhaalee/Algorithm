prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)-1):
            ans = max(ans,max(prices[i+1:])-prices[i])
        return ans


import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price-min_price)
        
        return profit
