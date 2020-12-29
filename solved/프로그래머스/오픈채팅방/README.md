### 정규표현식 - [오픈채팅방](https://programmers.co.kr/learn/courses/30/lessons/42888)

### 풀이

* 정규표현식 활용

```Python
import re

msg = 'junha님이 들어왔습니다.'

p = re.compile('[a-zA-Z0-9]+')

k = p.findall(msg)

k >>> ['junha']

```

