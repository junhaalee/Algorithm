### LeetCode - [Design HashMap](https://leetcode.com/problems/design-hashmap/)

### 풀이

* defaultdict(자료형) : key 값에 대응하는 value가 없을 경우, 입력한 자료형 타입의 데이터를 생성

```Python
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

        
class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)
        """
        Initialize your data structure here.
        """

    def put(self, key: int, value: int) -> None:
        # index : 해시값
        # %self.size : 해시함수
        index = key%self.size

        # 인덱스에 노드가 없을 때
        if self.table[index].value is None:
            self.table[index] = ListNode(key,value)
            return

        # 인덱스에 노드가 있을 때
        p = self.table[index]

        while p:
            # 이미 키가 있는 경우, value 업데이트
            if p.key == key:
                p.value = value
                return
            # 다음 노드가 없는 경우, 중단하고 새로운 노드 생성
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)        
        """
        value will always be non-negative.
        """
        
    def get(self, key: int) -> int:
        index = key%self.size
        
        # self.table[index].value가 None이라는 뜻은 defaultdict로 인해 생성된 ListNode가 하나 있다는 뜻.
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        # 주어진 key를 갖는 노드가 없을 경우 return -1
        return -1
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

    def remove(self, key: int) -> None:
        index = key%self.size
        if self.table[index].value is None:
            return
        
        p = self.table[index]
        # p가 Linked List의 첫번째 노드일 경우,
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
        # p가 Linked List의 중간에 있을 경우,
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev,p = p, p.next
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
```
