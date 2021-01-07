### LeetCode - [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

### 풀이

* 힙이란 ?
* 최댓값과 최솟값을 빠르게 찾기 위해 고안된 자료구조로, 각 노드의 key 값이 해당 노드의 자식 노드의 key 값보다 작지 않거나 크지 않은 완전이진트리
* 
* 최대 힙(Max heap) : 부모 노드의 key 값이 자식 노드의 key 값보다 작지 않은 힙
* 최소 힙(Min heap) : 부모 노드의 key 값이 자식 노드의 key 값보다 크지 않은 힙
* 
* Python의 heapq 모듈은 Min heap

```Python

# heap
import heapq
heap = []
# heapify : 리스트를 힙으로 변환
heapq.heapify(heap)
# heappush(heap, val) : 힙에 val 삽입
heapq.heappush(heap, 3)
# heappop(heap) : return heap[0]
heapq.heappop(heap)
# heappushpop(heap,val) : 힙에 val 삽입하는 동시에 return heap[0]
heapq.heappushpop(heap,4)

# 1. 나의 풀이 - 96ms / 18.4MB
# 배열에 모든 숫자를 담은 뒤에 배열 정렬하고 새로운 node들 생성
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        nums =[]
        
        for list in lists:
            while list:
                nums.append(list.val)
                list = list.next
        
        if not nums:
            return None
        
        nums.sort()
        root = head = ListNode(None)
        root.next = head
        
        for num in nums:
            head.next = ListNode(num)
            head = head.next
        
        return root.next


# 2. 힙을 사용한 풀이 - 92ms / 18.1MB
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []
        
        # 첫번째 노드들만 일단 heap에 넣어주기
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val, i, lists[i]))
        
        while heap:
            node = heapq.heappop(heap)
            index = node[1]
            result.next = node[2]
            
            result = result.next

            # result가 마지막 노드가 아니라면, 다음 노드 다시 heap에 넣기    
            if result.next:
                heapq.heappush(heap,(result.next.val, index, result.next))
            
        return root.next
```