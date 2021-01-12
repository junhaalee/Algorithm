### LeetCode - [Network Delay Time](https://leetcode.com/problems/network-delay-time/)

### 풀이

* 다익스탈 알고리즘 기본

```Python
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # 출발 노드, 도착 노드, 소요시간 저장
        graph = defaultdict(list)
        
        for s,e,t in times:
            graph[s].append([e,t])
            
        # 출발 노드부터 출발 노드는 소요시간 0 -> 저장
        Q = [(0,k)]
        dist = defaultdict(int)
        
        while Q:
            # 출발 노드에서부터 가장 빨리 도착한 노드부터 탐색 시작
            time, node = heapq.heappop(Q)
            
            if node not in dist:
                dist[node] = time
                for no,t in graph[node]:
                    # new_time 갱신
                    new_time = time + t
                    heapq.heappush(Q, (new_time, no))
        
        # 모든 노드에 대한 순회가 가능한지 확인
        if len(dist) == n:
            return max(dist.values())
        
        return -1 

```