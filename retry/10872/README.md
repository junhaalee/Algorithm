### 백준 10872 - [팩토리얼](https://www.acmicpc.net/problem/10872)

### 재귀의 가장 대표적인 형태

* 재귀의 형태를 기억하자

```Python
n = int(input())

def sol(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*sol(n-1)

print(sol(n))
```

