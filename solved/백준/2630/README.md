### 백준  - [2630](https://www.acmicpc.net/problem/2630)

### 풀이

* 기준 위치와 길이를 정해준 후에 재귀 응용

```Python
sol(x+k//2,y,k//2,ans)
sol(x,y+k//2,k//2,ans)
sol(x+k//2,y+k//2,k//2,ans)
sol(x,y,k//2,ans)
```

