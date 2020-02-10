### 백준  - [2798](https://www.acmicpc.net/problem/2798)

### 풀이

* 조합이 필요할 때에는 combinations, 순열이 필요할 때에는 permuation. 

```Python
from itertools import combinations

n, k = map(int, input().split())

nums = list(map(int, input().split()))

case = list(combinations(nums, 3))

ans = 0
for c in case:
    if sum(c) <= k and sum(c) > ans:
        ans = sum(c)

print(ans)
```

