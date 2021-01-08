J = 'aA'
S = 'aAAbbbb'

from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter_s = Counter(S)   
        sum = 0
        for j in J:
            if j in counter_s:
                sum += counter_s[j]
        return sum

sol = Solution()
sol.numJewelsInStones(J,S)

