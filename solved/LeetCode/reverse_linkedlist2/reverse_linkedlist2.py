# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = current = ListNode(None)
        root.next = head

        for _ in range(m-1):
            current = current.next
        
        end = start.next

        for _ in range(n-m):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
        
        return root.next