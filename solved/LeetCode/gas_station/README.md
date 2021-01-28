### LeetCode - [Gas Station](https://leetcode.com/problems/gas-station/)

### 풀이

* O(n^2) : 4680ms
* O(n) : 56ms

```Python

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0,0

        for i in range(len(gas)):
            if gas[i]+fuel < cost[i]:
                # 원형이기 때문에 조건을 만족하지 않으면 한 칸 뒤로 밀어버리기
                start = i+1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        
        return start

```

