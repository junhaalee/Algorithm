# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        q = []

        node = l1
        while node != None:
            q.append(node.val)
            node = node.next
        
        node = l2
        while node != None:
            q.append(node.val)
            node = node.next

        if q: 
            q.sort()

            l = ListNode(q.pop(),None)
            
            while q :
                l = ListNode(q.pop(),l)

            return l

        else:
            return None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next,12)
        return l1