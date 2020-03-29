### 백준  - [6996](https://www.acmicpc.net/problem/6996)

### 풀이

* sorted() 함수를 이용하면 문자 정렬도 가능하다.

```Python
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a,b = input().split()
    print(a+' & '+b+' are anagrams.') if sorted(list(a)) == sorted(list(b)) else  print(a+' & '+b+' are NOT anagrams.')
```

