### LeetCode - [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/)

### 풀이

* ListNode를 이용한 이중 연결 리스트
* head / tail / left / right

```Python
class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
    
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.right = n
        n.left = new
        new.left = node

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node


    def insertFront(self, value: int) -> bool:
        if self.k == self.len:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        

    def insertLast(self, value: int) -> bool:
        if self.k == self.len:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1
        """
        Get the front item from the deque.
        """
        

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1
        """
        Get the last item from the deque.
        """
        
    def isEmpty(self) -> bool:
        return self.len == 0
        """
        Checks whether the circular deque is empty or not.
        """
        

    def isFull(self) -> bool:
        return self.len == self.k
        """
        Checks whether the circular deque is full or not.
        """
        
```