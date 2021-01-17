### LeetCode - [Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)

### 풀이

* 트리 순회 개념과 비슷
*     A
*   /   \ 
*  B     C
* C = C
* A = A+C
* B = A+B+C

```Python

class Solution:
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:

        if root:
            # 오른쪽 서브 트리 먼저 탐색
            self.bstToGst(root.right)
            # self.val은 누적값 root.val은 현재 노드값
            self.val += root.val
            root.val = self.val
            # 왼쪽 서브 트리 갱신
            self.bstToGst(root.left)
        
        return root
```

