### LeetCode - [Minimum Height of Trees](https://leetcode.com/problems/minimum-height-trees/)

### 풀이

* 리프 노드를 제거해나가면, 마지막에 남은 노드가 가장 중앙에 있는 노드가 되겠지

```Python

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = defaultdict(list)

        # 우선 그래프로 만들어주기
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # 리프 노들 구하기
        # 리프 노드는 하나의 노드하고만 연결되어있을 것이기 때문에 길이 1
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 최종 노드가 2개 이하로 남을 때까지 반복
        while n > 2:

            n -= len(leaves)

            new_leaves = []

            for leaf in leaves:
                # 리프 노드와 연결되어 있는 neighbor
                neighbor = graph[leaf].pop()
                # neighbor에서 리프 노드와의 연결 제거
                graph[neighbor].remove(leaf)

                # neighbor가 리프 노드라면 new leaves에 추가
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves
        
        return leaves
```

