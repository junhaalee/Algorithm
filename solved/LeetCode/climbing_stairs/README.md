### LeetCode - [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

### 풀이

* 피보나치
* 재귀보다 DP가 속도가 빠름

```Python
from collections import defaultdict
class Solution:
    dp = defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            self.dp[n] = n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n-1)+self.climbStairs(n-2)

        return self.dp[n]

```

