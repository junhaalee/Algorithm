class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points = sorted(points, key = lambda x : x[0]**2+x[1]**2)
        return points[:K]

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