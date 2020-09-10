### 프로그래머스 - [징검다리 건너기](https://programmers.co.kr/learn/courses/30/lessons/64062)

### 풀이

* 이분탐색 활용

```Python

    while(left+1 < right):

        mid = (left+right)//2

        if check(stones, k, mid):
            left = mid
        else:
            right = mid

```

