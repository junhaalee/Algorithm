### 백준  - [2231](https://www.acmicpc.net/problem/2231)

### 풀이

* while을 쓸 때에는 항상 종료 조건을 빠짐없이 생각해줄 것.

```Python
n = int(input())

i = 1
while(True):
    
    if i > n:
        print(0)
        break
    
    if i+sum(map(int, list(str(i)))) == n:
        print(i)
        break
    i += 1
```

