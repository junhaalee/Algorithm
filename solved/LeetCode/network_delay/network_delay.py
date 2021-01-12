times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4 
k = 2
import heapq
class Solution:
    # def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    def networkDelayTime(self, times, n: int, k: int):
        graph = defaultdict(list)

        for a,b,c in times:
            graph[a].append([b,c])
        
        #(소요시간, 정점)
        Q = [(0,k)]
        dist = defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for no, t in graph[node]:
                    alt = time + t
                    heapq.heappush(Q, (alt,no))
        
        if len(dist) == n:
            return max(dist.values())
        return -1

sol = Solution()
sol.networkDelayTime(times,n,k)
