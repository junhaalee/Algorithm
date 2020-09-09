### 프로그래머스 - [파일명 정렬](https://programmers.co.kr/learn/courses/30/lessons/17686)

### 풀이

* 정규표현식 사용

```Python
import re

p = re.compile('[0-9]+')  자릿수 상관없이 모든 숫자

p = re.compile('[a-z][A-Z]+') #문자열 길이 상관없이 모든 영문자
```

