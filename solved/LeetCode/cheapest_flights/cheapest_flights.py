flights = [[0,1,100],[1,2,100],[0,2,500]]
n,src,dst,k = 3,0,2,1


flights = [[0,1,100],[1,2,100],[0,2,500]]
n,src,dst,k = 3,0,2,0

flights = [[0,1,10],[1,2,10],[0,3,1],[3,4,1],[4,2,1]]
n,src,dst,K = 5,0,2,3

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
         
        graph = defaultdict(list)

        for s,d,t in flights:
            graph[s].append([d,t])
        
        c = 0
        Q = [(0,src,c)]
        

        while Q:

            time, node, c = heapq.heappop(Q)

            if node == dst:
                print(time)
                break
            
            if c <= K:
                c += 1

                for d,t in graph[node]:
                    heapq.heappush(Q,(time+t,d,c))
        
        print(-1)