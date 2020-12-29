### 백준  - [11279](https://www.acmicpc.net/problem/11279)

### 풀이

* 기본적으로 heap은 min heap(pop을 할 경우 작은 수부터 나오는) 구조이지만, 이 문제는 max heap으로 바꿔서 해결해야하는 문제 - 유용하게 쓰일 듯.
* import sys는 거의 필수라고 생각하고 사용하자.
* heap 참고 : https://www.daleseo.com/python-heapq/


```Python
import heapq
import sys
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    k = int(input())

    if k == 0:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,-k)
```

