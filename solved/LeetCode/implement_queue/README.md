### LeetCode - [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

### 풀이

* Queue는 FIFO(First In First Out)

```Python

class MyQueue:

    def __init__(self):
        self.q = list()
        """
        Initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        self.q.append(x)
        """
        Push element x to the back of queue.
        """
        

    def pop(self) -> int:
        data = self.q[0]
        self.q = self.q[1:]
        return data
        """
        Removes the element from in front of queue and returns that element.
        """
        

    def peek(self) -> int:
        return self.q[0]
        """
        Get the front element.
        """
        

    def empty(self) -> bool:
        return len(self.q) == 0
        """
        Returns whether the queue is empty.
        """
    
```