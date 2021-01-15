### LeetCode - [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

### 풀이

* 재귀 활용
* 자식 노드가 있다면 계속 dfs 함수 타고 탐색
* 자식 노드가 없어진 순간부터 dfs 종료되고 다시 순차적으로 진행

```Python
class Solution:
    
    longest = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            # 리프 노드의 자식 노드에게 -1을 할당
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)
            
            # 리프노드 찾았으면 다시 타고 올라오기
            # longest는 경로의 길이
            self.longest = max(self.longest, left+right+2)
            # return 상태값(리프부터 현재 노드까지의 길이)
            return max(left,right)+1
        
        dfs(root)

        return self.longest

```