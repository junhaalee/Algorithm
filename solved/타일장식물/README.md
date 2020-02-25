### 프로그래머스  - [타일장식물](https://programmers.co.kr/learn/courses/30/lessons/43104?language=python3)

### 풀이

* 피보나치

```Python
def solution(N):
    if N == 1:
        return 4
    elif N == 2:
        return 6
    else:
        return solution(N-1)+solution(N-2)
```

