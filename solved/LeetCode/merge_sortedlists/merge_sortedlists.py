# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        nums =[]
        
        for list in lists:
            while list:
                nums.append(list.val)
                list = list.next
        
        if not nums:
            return None
        
        nums.sort()
        root = head = ListNode(None)
        root.next = head
        
        for num in nums:
            head.next = ListNode(num)
            head = head.next
        
        return root.next

# heap 사용
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val, i, lists[i]))
        
        while heap:
            node = heapq.heappop(heap)
            index = node[1]
            result.next = node[2]
            
            result = result.next
            
            if result.next:
                heapq.heappush(heap,(result.next.val, index, result.next))
            
        return root.next