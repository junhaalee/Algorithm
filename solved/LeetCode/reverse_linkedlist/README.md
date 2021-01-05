### LeetCode - [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

### 풀이

* prev -> current, current -> next, next -> current.next 구조
* current.next = prev로 해줌으로써 prev는 Linked List 구조 유지

```Python

# 1. 내 풀이 - 32ms / 15.7MB
# 런너 기법 때 사용했던 rev를 이용
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next
        return rev


# 2. 재귀
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(current: ListNode, prev: ListNode = None):
            if not current:
                return prev
            # 원래는 prev-node-next 순인데, node.next = prev로 지정해줌으로써 reverse 만들기
            next, current.next = current.next, prev
            return reverse(next,current)

        return reverse(head)


# 3. 반복 구조로 뒤집기 
# 런너 기법과 거의 동일, 재귀랑도 비슷
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current, prev = head, None

        while node:
            next, current.next = current.next, prev
            prev, current = current, next

        return prev
```