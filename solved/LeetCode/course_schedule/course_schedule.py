numCourses = 2
prerequisites = [[0,1],[0,2],[1,2]]

# visited 없을 때
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        visit = set()

        def dfs(num):

            if num in visit:
                return False
            
            visit.add(num)
            
            print('구역1')
            print(visit)
            
            for k in graph[num]:
                if not dfs(k):
                    return False

            print('구역2')
            print(visit)
            
            visit.remove(num)

            print('구역3')
            print(visit)

            return True
        
        for num in list(graph):
            if not dfs(num):
                return False
        
        return True


# visited 있을 때

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        visit = set()
        visited = set()

        def dfs(num):

            if num in visit:
                return False

            if num in visited:
                return True

            visit.add(num)

            for k in graph[num]:
                if not dfs(k):
                    return False
            
            visit.remove(num)

            visited.add(num)
            print(visited)
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True


sol = Solution()
sol.canFinish(numCourses,prerequisites)

