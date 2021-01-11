tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

# DFS
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):

        dic = defaultdict(list)

        for a,b in sorted(tickets):
            dic[a].append(b)

        path = []

        def dfs(city):

            while dic[city]:
                dfs(dic[city].pop(0))

            path.append(city)
            
        dfs('JFK')

        return path[::-1]

# pop
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):

        dic = defaultdict(list)

        for a,b in sorted(tickets, reverse=True):
            dic[a].append(b)

        path = []

        def dfs(city):
            while dic[city]:
                dfs(dic[city].pop())

            path.append(city)
            
        dfs('JFK')

        return path[::-1]


# 스택
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):

        dic = defaultdict(list)

        for a,b in sorted(tickets, reverse=True):
            dic[a].append(b)
        
        stack = ['JFK']
        path = []
        
        while stack:
            while dic[stack[-1]]:
                stack.append(dic[stack[-1]].pop())
            path.append(stack.pop())
        
        return path[::-1]