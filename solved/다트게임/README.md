### 프로그래머스 - [다트게임](https://programmers.co.kr/learn/courses/30/lessons/17682)

### 풀이

* 문자열에서 특정한 패턴을 찾으려면, 정규표현식을 사용하자
* Python 문서에 정규표현식 추가

```Python
#정규표현식 사용한 코드

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*':
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

```

