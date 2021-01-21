### LeetCode - [Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/)

### 풀이

* Insertion Sort

```Python

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        cur = parent = ListNode(0)

        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next
            
            if head and cur.val > head.val:
                cur = parent
        
        return parent.next

```

