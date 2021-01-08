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
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)        
        """
        value will always be non-negative.
        """
        

    def get(self, key: int) -> int:
        index = key%self.size
        
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
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
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)