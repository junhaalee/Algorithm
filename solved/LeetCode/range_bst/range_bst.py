# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        if root and (low <= root.val <= high):
            self.val += root.val
        
        if root:
            self.rangeSumBST(root.left,low,high)
            self.rangeSumBST(root.right,low,high)

        return self.val
        