### LeetCode - [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

### 풀이

* 다익스트라 활용
* 핵심은 우선순위 큐

```Python

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
         
        graph = defaultdict(list)

        for s,d,t in flights:
            graph[s].append([d,t])
        
        # c는 경유지 개수
        c = 0
        Q = [(0,src,c)]

        while Q:

            time, node, c = heapq.heappop(Q)

            # 가장 이른시간에 dst에 도착했을 때 return time
            if node == dst:
                return time
            
            # 경유지 개수 초과했으면 탐색 X
            if c <= K:
                c += 1

                for d,t in graph[node]:
                    heapq.heappush(Q,(time+t,d,c))
        
        return -1

```