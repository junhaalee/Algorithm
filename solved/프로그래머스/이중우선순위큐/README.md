### 프로그래머스 - [이중우선순위큐](https://programmers.co.kr/learn/courses/30/lessons/42628)

### 풀이

* 파이썬의 heapq는 최소 힙(min heap - 최소값은 배열의 가장 첫번째 위치에 있지만, 최대값은 모름.)만 지원.
* deque 사용.

```Python
#최대 힙으로 활용하는 경우 --> 배열의 최대값이 가장 첫번째 위치에 있음.
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1

```

