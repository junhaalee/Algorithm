### 백준  - [11286](https://www.acmicpc.net/problem/11286)

### 풀이

* abs() 함수를 이용하면 절댓값을 알 수 있음 - abs heap

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
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    
    else:
        heapq.heappush(heap,(abs(k),k))
```

