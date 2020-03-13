### 백준  - [1010](https://www.acmicpc.net/problem/1010)

### 풀이

* 순열/조합을 알고있으면 간단하게 풀 수 있었던 문제.

```Python
    for i in range(m,m-n,-1):
        answer *= i
    for i in range(n,1,-1):
        answer //= i
```

