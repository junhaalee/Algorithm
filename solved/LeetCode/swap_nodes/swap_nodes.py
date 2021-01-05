# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        current = head

        while current and current.next:
            current.val, current.next.val = current.next.val, current.val
            current = current.next.next
        
        return head
            
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(0)

        prev.next = head

        # prev - head - b
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            prev.next = b

            # 다시 prev, head setting
            head = head.next
            prev = prev.next.next
        
        return root.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            # head - p
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head