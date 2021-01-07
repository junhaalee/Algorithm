### LeetCode - [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

### 풀이

* enQueue : 원소 삽입
* deQueue : 원소 제거
* Front : front 자리에 있는 원소 return
* Rear : rear 자리에 있는 원소 return

```Python
class MyCircularQueue:

    # 처음에는 front, rear 둘 다 0
    def __init__(self, k: int):
        self.q = [None]*k
        self.maxlen = k
        self.front = 0
        self.rear = 0
        
    # rear가 None이라면, 즉 빈 공간이 있다면 삽입
    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear+1)%self.maxlen
            return True
        else:
            return False

    # front가 None이 아니라면, 즉 원소가 하나라도 존재한다면 front 자리에 있는 원소 제거
    def deQueue(self) -> bool:
        if self.q[self.front] is not None:
            self.q[self.front] = None
            self.front = (self.front+1)%self.maxlen
            return True
        else:
            return False

    # front 자리에 있는 원소가 None이라면, 즉 큐가 비어있다면 return -1
    # 아니라면 front 자리에 있는 원소 return
    def Front(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.q[self.rear-1] is None else self.q[self.rear-1]

    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None
        
    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None

```
* a = 0
* b = None
* return a -> False
* return b -> False