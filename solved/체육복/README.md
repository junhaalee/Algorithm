### 프로그래머스  - [체육복](https://programmers.co.kr/learn/courses/30/lessons/42862)

### 풀이

* lost와 reserve에 모두 속해있는 학생의 경우에는 처음부터 경우의 수에서 배제해주어야 한다. 그리고 answer += 1.
* 그래야 머리가 안아프다

```Python
    for k in range(len(lost)):
        for i in range(len(reserve)):
            if lost[k] == reserve[i]:
                lost[k],reserve[i] = 45,35
                answer += 1
```

* 다른 사람의 풀이
```Python
def solution(n, lost, reserve):
    reserved = 0
    lostN = list(set(lost) - set(reserve))
    reserveN = list(set(reserve) - set(lost))
    lostN.sort()
    for l in lostN:
        for x in range(l-1, l+2):
            if x in reserveN:
                reserveN.remove(x)
                reserved += 1
                break
    return n - len(lostN) + reserved
```
