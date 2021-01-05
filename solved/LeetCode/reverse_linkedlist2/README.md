### LeetCode - [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

### 풀이

* Reverse Linked List와 비교

```Python
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = current = ListNode(None)
        root.next = head

        # reverse가 필요한 바로 앞까지 이동
        for _ in range(m-1):
            current = current.next
        
        # reverse의 마지막이 될 node 지정
        end = start.next

        # start와 end는 고정한 상태로 tmp를 이동시켜가면서 reverse
        # 변수 = 의 의미는 노드 지정
        # 변수.next = 의 의미는 화살표 그려주기
        for _ in range(n-m):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
        
        # start,end는 고정시키기로 했으니깐, 다시 대입하지 않음
        # tmp는 계속 바뀌니깐 계속 다시 대입.
        return root.next

```