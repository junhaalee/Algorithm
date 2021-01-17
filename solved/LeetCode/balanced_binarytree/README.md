### LeetCode - [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

### 풀이

* 판단 조건을 명확하게 파악하고 적용해줘야 한다
* if left == -1 or right == -1 or abs(left-right) > 1:
* 이 부분에서 조건 명시 정확하게 안해줘서 계속 틀렸음

```Python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        def dfs(node):
            # 리프 노드의 자식들 만나면 return 0    
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # left, right 둘 중 하나가 이미 탈락이거나
            # 현재 노드에서 탈락일 경우, return -1
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            
            # 탈락 아닐 경우에는 정상적으로 return 
            return max(left,right)+1
                    
        return dfs(root) != -1

```