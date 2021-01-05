### LeetCode - [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

### 풀이

* 다중 할당 : 2개 이상의 값을 2개 이상의 변수에 동시에 할당하는 것.

```Python

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        while even and even.next:
            
            # 1->2->3->4->5
            # 다중 할당을 했을 때와 하지 않았을 때의 차이점을 알고 있어야함.
            # odd.next, odd = odd.next.next(3), odd.next(2)
            # even.next, even = even.next.next(4), even.next(3)
            # -> 이럴 경우 odd에 2가 할당됨. even도 마찬가지.
            
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        
        odd.next = even_head
        return head
        
```