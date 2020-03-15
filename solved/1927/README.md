### 백준  - [1927](https://www.acmicpc.net/problem/1927)

### 풀이

* 11279번이 max heap을 이용하는 문제라면, 이 문제는 min heap(heap 본연의 모습)을 이용하는 문제.

```Python
import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):

    k = int(input())

    if k == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,k)
```

