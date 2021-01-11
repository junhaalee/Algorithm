### LeetCode - [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

### 풀이

* 프로그래머스 여행경로와 똑같은 문제
* https://programmers.co.kr/learn/courses/30/lessons/43164

* 재귀 활용

```Python
# 다른 문제에서도 활용하기
# 테넷같다
def dfs(city):
    while dic[city]:
        # 1->2->3
        dfs(dic[city].pop(0))
    # 3->2->1
    path.append(city)

# 1. DFS
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):

        dic = defaultdict(list)

        for a,b in sorted(tickets):
            dic[a].append(b)

        path = []

        def dfs(city):

            # 알파벳 순서대로 pop
            while dic[city]:
                dfs(dic[city].pop(0))

            # 역순으로 city 저장
            path.append(city)
            
        dfs('JFK')

        # 마지막에 다시 역순으로 만들어주고 return
        return path[::-1]


# 2. pop(0) 대신 pop() 사용하기
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):

        dic = defaultdict(list)

        for a,b in sorted(tickets, reverse=True):
            dic[a].append(b)

        path = []

        def dfs(city):

            # 알파벳의 역순으로 정렬했기 때문에 1과 과정은 동일
            while dic[city]:
                dfs(dic[city].pop())

            path.append(city)
            
        dfs('JFK')

        return path[::-1]


# 3. 스택
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
            # 경로가 끊기는 경우, 스택값을 다시 받아와서 풀어야됨......
            path.append(stack.pop())
        
        return path[::-1]
```

