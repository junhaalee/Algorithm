from collections import defaultdict

class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n-1)+self.fib(n-2)


class Solution:
    dp = defaultdict(int)
    def fib(self, n):
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n-1)+self.fib(n-2)
        
        return self.dp[n]


class Solution:
    dp = defaultdict(int)
    def fib(self, n):
        if n <= 1:
            self.dp[n] = n
        
        for i in range(2, n+1):
            self.dp[n] = self.dp[n-1]+self.dp[n-2]
        
        return self.dp[n]