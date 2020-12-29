### 백준  - [10870](https://www.acmicpc.net/problem/10870)

### 풀이

* 팩토리얼과 비슷한 형태. 팩토리얼을 '곱하기'이기 때문에 0을 1로 처리해줌. 여기서는 1,0 모두 n으로 처리해도 상관없음. '더하기'이기 때문에
 

```Python
n = int(input())

def sol(n):
    if n == 0 or n == 1:
        return n
    else:
        return sol(n-1)+sol(n-2)

print(sol(n))
```

