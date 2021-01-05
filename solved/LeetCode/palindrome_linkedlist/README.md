### LeetCode - [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

### 풀이

* 스택의 pop(0) 시간복잡도 : O(n) - 164ms
* 데크의 popleft() 시간복잡도 : O(1) - 72ms
* 데크가 짱

```Python

# 1. 내 풀이 - 스택
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # ListNode의 val들을 넣어줄 리스트
        q: List = []

        # ListNode가 비어있다면 return True
        if not head:
            return True

        # Node(val, next)
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        # 양쪽 끝을 비교
        while len(q) > 1:
            if q.pop() != q.pop(0):
                return False
        
        return True

# 2. Deque를 이용한 풀이
from collections import deque
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # ListNode의 val들을 넣어줄 Deque
        q: Deque = deque()

        # ListNode가 비어있다면 return True
        if not head:
            return True

        # Node(val, next)
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        # 양쪽 끝을 비교
        while len(q) > 1:
            # pop(0) 대신 popleft()
            if q.pop() != q.popleft():
                return False
        
        return True
```

