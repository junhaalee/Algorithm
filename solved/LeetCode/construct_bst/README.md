### LeetCode - [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

### 풀이

![참고](./solved/img/img1.jpg)

* 분할 정복 문제로 바뀐다

```Python

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # 루트 지정
            index = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[index])

            # 재귀를 이용한 서브트리
            node.left = self.buildTree(preorder,inorder[:index])
            node.right = self.buildTree(preorder,inorder[index+1:])

        return node

```

