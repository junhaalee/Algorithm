### 백준  - [타겟넘버](https://programmers.co.kr/learn/courses/30/lessons/43165)

### 풀이

* numbers에 있는 숫자들을 하나씩 더하고 빼가면서 최종 terminal node에 들어갈 숫자들만 구한다 --> target 숫자를 찾는다.
* 다소 비효율적이라고 생각했는데, 일단은 통과했다.

```Python
def solution(numbers, target):

    ans = [0]

    for num in numbers:
        temp = []
        for a in ans:
            temp.append(a+num)
            temp.append(a-num)
        ans = temp

    answer = temp.count(target)

    return answer
```

