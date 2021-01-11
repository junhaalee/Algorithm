### LeetCode - [Course Schedule](https://leetcode.com/problems/course-schedule/)

### 풀이

* 그래프가 순환 구조인지를 판별하는 풀이
* 가지치기 방법은 visited를 이해하기가 많이 어려웠다...

```Python

# 계속 헷갈리는 부분
def test(n):
    if n == 1:
        return True
    print('구역 1 : '+str(n))
    test(n-1)
    print('구역 2 : '+str(n))

test(3)
# >>> 구역 1: 3
# >>> 구역 1: 2
# >>> 구역 2: 2
# >>> 구역 2: 3


# 1. DFS
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        # 순환 구조를 파악하는 풀이이니깐
        # visit에 이미 있는 원소를 또 방문하면 순환구조라는 뜻 -> return False
        visit = set()

        def dfs(num):
            # visit에 이미 있는 원소를 또 방문하면 순환구조라는 뜻 -> return False
            if num in visit:
                return False
            
            # visit에 없다면, 추가시키고 탐색 시작
            visit.add(num)

            # graph[num]의 원소들을 DFS 방식으로 탐색. 중간에 False 있으면 바로 return False
            for k in graph[num]:
                if not dfs(k):
                    return False

            # 부모 노드를 통해 탐색했을 경우가 아닌, 형제 노드를 통해 탐색하여 visit에 num이 계속 있을 경우에
            # 순환구조가 아님에도 불구하고 순환구조라고 return 할 수 있으므로, visit에서 제거
            visit.remove(num)

            return True
        
        for num in list(graph):
            if not dfs(num):
                return False
        
        return True


# 2. 가지치기
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        # visit은 탐색 중에 그래프가 순환인지 아닌지 확인하려는 용도
        # visited는 탐색이 종료된 노드를 저장. 또 다른 경로를 통해 해당 노드에 접근하여서 탐색하려는 경우, 이 노드는 이미 순환을 하지 않는 그래프를 구성하고 있다는 것을 알려주기 위한 용도
        visit = set()
        visited = set()

        def dfs(num):
            if num in visit:
                return False

            # 더이상의 탐색은 의미가 없음. 무조건 True다.
            if num in visited:
                return True

            visit.add(num)

            for k in graph[num]:
                if not dfs(k):
                    return False
            
            visit.remove(num)

            # 적어도 num이라는 노드로 부터 뻗어나가는 그래프는 순환을 하지 않음
            # 더이상의 탐색은 의미가 없다는 것을 알려주기 위해서
            visited.add(num)

            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True
```

