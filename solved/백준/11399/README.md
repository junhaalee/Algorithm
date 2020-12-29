### 백준  - [11399](https://www.acmicpc.net/problem/11399)

### 풀이

* 정렬

```Python
n = int(input())
time = sorted(list(map(int, input().split())))

ans = 0
for i in range(len(time)):
    ans += (time[i]*(len(time)-i))

print(ans)
```

