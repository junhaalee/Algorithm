### 프로그래머스 - [방금그곡](https://programmers.co.kr/learn/courses/30/lessons/17683)

### 풀이

* 시간계산 - datetime

```Python
from datetime import datetime

FMT = '%H:%M'  #시간 형식 지정

start = '12:00'
finish = '13:12'

time = datetime.strptime(finish,FMT) - datetime.strptime(start,FMT) # 초 단위로 환산됨.
```

