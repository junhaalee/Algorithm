### LeetCode - [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

### 풀이

```Python

# 1. 내 풀이
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

        # 계산 결과를 다시 Linked List 형태로 만들어주기
        n = None
        while sum:
            n = ListNode(sum.pop(),n)

        return n


# 2. 자료형 변환 없이 자리 올림으로 계산
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while carry or l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum +=  l2.val
                l2 = l2.next
            carry, val = divmod(sum+carry, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next

```

* 시간상으로는 별 차이가 없지만 훨씬 깔끔한 방법.