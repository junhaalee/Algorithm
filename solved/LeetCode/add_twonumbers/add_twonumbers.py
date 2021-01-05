# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = num2 = ''
        
        while l1 :
            num1 += str(l1.val)
            l1 = l1.next
        
        while l2 :
            num2 += str(l2.val)
            l2 = l2.next
        
        sum = list(str(int(num1[::-1])+int(num2[::-1])))

        n = None
        while sum:
            n = ListNode(sum.pop(),n)

        return n
