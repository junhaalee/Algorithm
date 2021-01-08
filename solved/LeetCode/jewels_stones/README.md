### LeetCode - [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)

### 풀이

* [s in jewels for s in stones] : [True, True, True, False, False]와 같은 형태의 배열이 만들어짐.
* sum([s in jewels for s in stones]) : sum은 True를 count

```Python

# 1. 내 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter_s = Counter(stones)   
        sum = 0
        for j in jewels:
            if j in counter_s:
                sum += counter_s[j]
        return sum

# 2. Pythonic Way
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([s in jewels for s in stones])

```

