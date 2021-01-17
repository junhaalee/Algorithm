### LeetCode - [Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)

### 풀이

* 트리 순회 응용
* result 값을 매번(조건에 맞을 경우) 갱신해줘야 함

```Python

# 1. 재귀
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    
    def minDiffInBST(self, root: TreeNode) -> int:
        # 왼쪽 탐사
        if root.left:
            self.minDiffInBST(root.left)

        # result와 이전 노드의 val과 현재 노드의 val 비교
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        
        # 오른쪽 탐사
        if root.right:
            self.minDiffInBST(root.right)
        
        return self.result


# 2. 반복
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        prev = -sys.maxsize
        result = sys.maxsize

        stack, node = [], root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()

            result = min(result, node.val-prev)
            prev = node.val

            node = node.right
        
        return result
```

