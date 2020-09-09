### 프로그래머스 - [프렌즈블록](https://programmers.co.kr/learn/courses/30/lessons/17679)

### 풀이

* numpy.transpose(list_name) 을 이용하면 list_name의 회전된 형태의 행렬을 구할 수 있다.

```Python
import numpy as np

a = [[0,0],[1,1]]

b = np.transpose(a)

b >>> [[0,1],[0,1]]
```

