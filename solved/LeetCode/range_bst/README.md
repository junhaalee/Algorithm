### LeetCode - [Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)

### 풀이

* 완전히 같은 방법을 다른 구조로 풀이하기
* 재귀, DFS, BFS

```Python

# 1. 내 풀이 - 384ms
class Solution:
    val = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        # root가 None이 아니고 조건을 만족하면 val update
        if root and (low <= root.val <= high):
            self.val += root.val
        
        # root가 None이 아니라면 왼쪽, 오른쪽 탐색
        if root:
            self.rangeSumBST(root.left,low,high)
            self.rangeSumBST(root.right,low,high)

        return self.val


# 2. 가지치기 - 200ms
class Solution:
    val = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        # root가 None이 아니고 조건을 만족하면 val update
        if root and (low <= root.val <= high):
            self.val += root.val
        
        # root가 None이 아니라면 왼쪽, 오른쪽 탐색
        if root:
            # root.val이 low보다 작거나 high보다 크다면 굳이 탐색 안해도 됨.
            if root.val > low:
                self.rangeSumBST(root.left,low,high)
            if root.val < high:
                self.rangeSumBST(root.right,low,high)

        return self.val


# 3. 재귀 대신 반복 구조 사용 - DFS - 200ms
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack, val = [root], 0
        
        while stack:

            node = stack.pop()

            if node:
                if low <= node.val <= high:
                    val += node.val
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return val


# 4. 재귀 대신 반복 구조 사용 - BFS - 268ms
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        queue, val = [root], 0
        
        while queue:

            node = queue.pop(0)

            if node:
                if low <= node.val <= high:
                    val += node.val
                if node.val > low:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
        return val
```
