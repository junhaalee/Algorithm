### 프로그래머스 - [2xN 타일링](https://programmers.co.kr/learn/courses/30/lessons/12900)

### 풀이

* 아주 쉬운 DP 문제 - 피보나치
* 최대한 효율적으로 - 시간 / 공간

```Python
def solution(n):

    answer = [1,2,3]

    for _ in range(n-3):
        del answer[0]
        answer.append(answer[-1]+answer[-2])

    return answer[-1]%1000000007
```

