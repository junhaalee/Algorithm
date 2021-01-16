### LeetCode - [Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)

### 풀이

* Diameter of Binary Tree와 유사함
* 재귀 활용

```Python
class Solution:
    
    result = 0
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        
        def dfs(node):

           # 리프 노드의 상태값 설정
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드와 왼쪽/오른쪽 자식 노드의 값 비교
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # left, 현재 노드, right가 모두 같은 값을 가질 경우, result는 left+right가 되어야 함
            self.result = max(self.result, left+right)

            # 그리고 현재 노드의 상태값은 left, right 중 최대값.
            # 현재 노드의 부모 노드는 하나의 경로만을 선택해야 하므로
            # 부모 노드 - 현재 노드 - left 또는 부모 노드 - 현재 노드 - right
            return max(left,right)
        
        dfs(root)

        return self.result

```