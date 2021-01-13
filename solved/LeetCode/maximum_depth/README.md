### LeetCode - [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

### 풀이

* 이진 트리 : 모든 노드의 차수가 2 이하인 트리

```Python

from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        # 처음에는 큐에 루트, 즉 노드 하나만 들어감
        queue = deque(root)
        depth = 0

        # 루트만 있어도 depth는 1이니깐
        while queue:

            depth += 1

            # len(queue)는 시작할 때 해당 level의 노드 개수만큼으로 고정.
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth

```