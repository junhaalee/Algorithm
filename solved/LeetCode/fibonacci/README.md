### LeetCode - [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

### 풀이

* 다이나믹 프로그래핑 방법론
* 상향식 접근법 : 타뷸레이션 - Tabulation
* 하향식 접근법 : 메모이제이션 - Memoization

```Python

# 재귀 
class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n-1)+self.fib(n-2)


# 메모이제이션 - 하향식 DP
class Solution:
    # 한번 계산한 값은 저장해두기
    dp = defaultdict(int)
    def fib(self, n):
        if n <= 1:
            return n

        # 이미 계산한 값이 있으면 그 값을 불러와서 계산 횟수를 줄일 수 있음
        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n-1)+self.fib(n-2)
        
        return self.dp[n]


# 테뷸레이션 - 상향식 DP
# 메모이제이션과 마찬가지로 계산한 값은 저장해두어서 계산 횟수를 줄일 수 있음
class Solution:
    dp = defaultdict(int)
    def fib(self, n):
        
        self.dp[0] = 0
        self.dp[1]  = 1       
        
        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1]+self.dp[i-2]
        
        return self.dp[n]


```
