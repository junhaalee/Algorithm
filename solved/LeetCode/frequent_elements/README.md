### LeetCode - [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

### 풀이

* zip() : 2개 이상의 시퀀스를 짧은 길이를 기준으로 같은 index에서 일대일 대응하는 새로운 튜플 시퀀스를 만드는 역할을 한다. 
* a = [1,2,3,4,5], b = [2,3,4,5], c = list(zip(a,b))
* c >>> [(1,2),(2,3),(3,4),(4,5)]   zip(a,b,c)도 가능
* 
* 아스테리스크(*) : unpack의 기능. 시퀀스 언패킹 연산자(Sequence Unpacking Operator)로 시퀀스를 풀어 헤치는 연산자를 뜻함. 주로 튜플이나 리스트를 언패킹하는 데 사용한다.
* a = [1,2,3,4]
* print(*a) >>> 1 2 3 4 
* 단, 함수의 parameter가 되었을 때는 반대로 패킹(Packing)도 가능
* '*' 1개는 튜플 또는 리스트 등의 시퀀스 언패킹 / '**' 2개는 키/값 페어를 언패킹하는데 사용


```Python

# 1. 내 풀이 - 164ms / 18.8MB
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [s[0] for s in Counter(nums).most_common(k)]

# 2. zip과 * 사용 - 140ms / 18.4MB
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
```
