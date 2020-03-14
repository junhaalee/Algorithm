### 백준  - [11053](https://www.acmicpc.net/problem/11053)

### 풀이

* num이 dp 배열의 역할

```Python
num = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            num[i] = max(num[i], num[j]+1)
```

