### LeetCode - [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/submissions/)

### 풀이

* 재귀 풀이 : l1과 l2의 값을 비교해서 작은 값이 왼쪽에 오게 하고, next는 그 다음 값이 엮이도록 재귀 호출하는 방법.

```Python

# 1. 내 풀이 - 36ms / 14.2MB
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

        # q라는 배열에 모든 element를 모으고 정렬
        if q: 
            q.sort()
            # 정렬한 뒤에 다시 LinkedList 형태로 만들어주기
            l = None
            
            while q :
                l = ListNode(q.pop(),l)

            return l
            
        else:
            return None


# 2. 재귀 - 36ms / 14.3MB
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next,l2)
        return l1

```