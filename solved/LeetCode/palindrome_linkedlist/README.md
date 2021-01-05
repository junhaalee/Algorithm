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


# 3. 런너 기법
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next :
            fast = fast.next.next
            # rev.next = rev : slow의 역순
            rev, rev.next, slow = slow, rev, slow.next
        
        # ListNode의 길이가 홀수일 경우, slow 한칸 앞으로 이동
        # 정가운데에 있는 숫자는 check의 범위에 포함되지 않으므로
        if fast:
            slow = slow.next
        
        # slow가 밟아온 길을 반대로 저장하고 있는 rev와
        # 중간을 넘어서 앞으로가는 slow를 비교
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        return not rev

```
* 런너(Runer) 기법
* 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법 - 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있음
* 빠른 런너는 두칸씩 이동, 느린 런너는 한칸씩 이도하여 빠른 런너가 리스트의 끝에 도달하면, 느린 런너는 정확히 리스트의 중간 지점을 가리키게 됨
* 중간 위치를 찾아내면, 여기서부터 값을 비교하거나 뒤집기를 시도하는 등의 활용이 가능
