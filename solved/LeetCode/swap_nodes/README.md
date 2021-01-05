### LeetCode - [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

### 풀이

* 내 풀이 : LinkedList 구조는 그대로 유지한 상태에서 노드 안의 값만 스와핑
* 2번, 3번 풀이 : LinkedList 안의 구조를 수정하는 형태 - Node와 Node를 스와핑

```Python

# 1. 내 풀이 - 32ms
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        current = head

        while current and current.next:
            current.val, current.next.val = current.next.val, current.val
            current = current.next.next
        
        return head

# 2. 반복 구조로 스왑
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(0)

        prev.next = head

        # prev - head - b
        while head and head.next:
            # swap해서 다시 연결
            b = head.next
            head.next = b.next
            b.next = head
            prev.next = b

            # 다시 prev, head setting
            head = head.next
            prev = prev.next.next
        
        return root.next


# 3. 재귀 구조로 스왑
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            # head - p
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head

```

