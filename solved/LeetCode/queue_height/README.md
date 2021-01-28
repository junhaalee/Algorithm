### LeetCode - [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/submissions/)

### 풀이

* 우선순위 큐 활용
* insert(index, element)

```Python
# 우선순위 큐
import heapq
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        heap = []

        # python은 min heap만 지원하기 때문에, 음수로 활용
        for p in people:
            heapq.heappush(heap, (-p[0],p[1]))
        
        result = []

        while heap:
            p = heapq.heappop(heap)
            result.insert(p[1],[-p[0],p[1]])

        return result

```

