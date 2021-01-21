### LeetCode - [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

### 풀이

* math.sqrt : 제곱근을 반환

```Python

# 1. 내 풀이 - 632ms
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points = sorted(points, key = lambda x : x[0]**2+x[1]**2)
        return points[:K]

# 2. Heap을 이용한 풀이
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x,y) in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist,x,y))
        result = []
        for _ in range(K):
            dist, x, y = heapq.heappop(heap)
            result.append([x,y])
        return result
```

