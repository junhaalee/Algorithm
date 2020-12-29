### 백준  - [2455](https://www.acmicpc.net/problem/2455)

### 풀이

* DP랑도 약간 비슷했던 문제.

```Python
import sys
input = sys.stdin.readline

ans = [0]*5

for ind in range(1,5):
    o,i = map(int, input().split())
    ans[ind] = ans[ind-1]-o+i
print(max(ans))
```

