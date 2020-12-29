### 프로그래머스 - [튜플](https://programmers.co.kr/learn/courses/30/lessons/64065)

### 풀이

* 정규표현식 사용
* Counter 사용

```Python
import re
from collections import Counter

def solution(s):

    a = dict(Counter(re.findall('\d+',s)))

    answer = [int(k[0]) for k in sorted(a.items(), key = (lambda x : x[1]), reverse = True)]

    return answer
```

