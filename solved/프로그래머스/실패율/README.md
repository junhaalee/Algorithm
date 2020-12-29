### 프로그래머스 - [실패율](https://programmers.co.kr/learn/courses/30/lessons/42889)

### 풀이

* Counter 사용하면 input으로 들어간 배열의 원소 갯수를 counting 해줌.

```Python
from collections import Counter

result = dict(Counter(stages))
```

