### 프로그래머스  - [큰수만들기](https://programmers.co.kr/learn/courses/30/lessons/42883)

### 풀이

* 방법 1 : combination 사용하기 - 시간 초과

```Python
from itertools import combinations

def solution(number, k):
    nums = list(number)
    
    temp = sorted(list(combinations(nums, len(number)-k)),reverse=True)

    answer = ''.join(list(temp[0]))
    
    return answer
```

* 방법 2 : string을 list로 만들어서  - 시간 초과

```Python
def solution(number, k):
    k = len(number)-k
    answer = []
    ind = 0

    while(True):
        if k == 0:
            break
        if k == 1:
            answer += max(number[ind:])
            ind += number[ind:].index(max(number[ind:]))
        else:
            answer += max(number[ind:-k+1])
            ind += number[ind:-k+1].index(max(number[ind:-k+1]))
        num[ind] = 0

        k -= 1
    
    return answer
```

* 방법 3 : 문자열 그대로 사용하기

```Python
def solution(number, k):
    answer = ''
    n,k = len(number)-k,len(number)-k

    while(True):
        if len(answer) == n:
            break
        if len(number) > k:
            if k == 1:
                answer += max(number[:])
            else:
                answer += max(number[:-k+1])
                ind = number.index(max(number[:-k+1]))
            number = number[ind+1:]
            k -= 1
        else:
            answer += number

    return answer
```