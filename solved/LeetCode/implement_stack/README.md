### LeetCode - [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

### 풀이

* Stack은 LIFO(Last in First Out)

```Python
from collections import deque
class MyStack:

    def __init__(self):
        self.s = deque()
        """
        Initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        self.s.appendleft(x)
        """
        Push element x onto stack.
        """
        

    def pop(self) -> int:
        data = self.s.popleft()
        return data
        """
        Removes the element on top of the stack and returns that element.
        """
        

    def top(self) -> int:
        return self.s[0]
        """
        Get the top element.
        """
        

    def empty(self) -> bool:
        return len(self.s) == 0
        """
        Returns whether the stack is empty.
        """
```