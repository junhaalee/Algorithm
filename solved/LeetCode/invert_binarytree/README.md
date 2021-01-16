### LeetCode - [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

### 풀이

* 재귀를 활용하겠다는 직감
* 다시 한 번 떠올렸다 BFS는 Queue / DFS는 Stack

```Python

# 1. 내 풀이
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        # left가 있다면 타고 들어가기
        if root.left:
            self.invertTree(root.left)
        # right가 있다면 타고 들어가기             
        if root.right:
            self.invertTree(root.right)

        # 서로 교환
        root.left, root.right = root.right, root.left

        return root


# 2. Pythonic
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.inverTree(root.left)

        return root


# 3. BFS - Queue
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:  
        queue = deque([root])

        while queue:
            # BFS는 Queue
            # Queue는 popleft-FIFO
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)

        return root


# 3. DFS - Stack
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:  
        stack = deque([root])

        while stack:
            # DFS는 Stack
            # Stack은 pop-LIFO
            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)

        return root
```

