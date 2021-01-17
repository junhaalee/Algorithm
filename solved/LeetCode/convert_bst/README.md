### LeetCode - [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

### 풀이

* BST의 특성을 이용 - 정렬
* nums의 가운데 값이 subtree의 root가 되면 된다

```Python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if not nums:
            return 
        
        # 가운데 값 찾기
        mid = len(nums)//2

        # mid를 value로 하는 노드 만들어주기
        node = TreeNode(nums[mid])
        # 재귀
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])

        return node

```

