### LeetCode - [Sort List](https://leetcode.com/problems/sort-list/)

### 풀이

* 

```Python
# 1. 내 풀이 - 내장 함수 사용하기 (더 빠름)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        p = head
        
        li = list()
        
        while p:
            li.append(p.val)
            p = p.next

        # list에 넣어준 후에 sort
        li.sort()
        
        # list를 다시 Linked List 형태로 만들어주기
        p = head
        
        for i in li:
            p.val = i
            p = p.next
        
        return head 


# 2. Merge Sort - 병합 정렬
class Solution:
    def mergesort(self, l1: ListNode, l2: ListNode):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergesort(l1.next, l2)
        
        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
 
        if not (head and head.next):
            return head
        
        # 런너 기법
        half, slow, fast = None, head, head
        while fast and fast.next:
            half = slow
            slow = slow.next
            fast = fast.next.next
        # 연결 리스트 끊어버리기
        half.next = None

        # 각각 끊어진 배열의 가장 첫번째 node
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergesort(l1,l2)

```

