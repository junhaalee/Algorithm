### 백준  - [1541](https://www.acmicpc.net/problem/1541)

### 풀이

* 

```Python
temp = input().split('-')
ans = sum(list(map(int, temp[0].split('+'))))
for i in range(1, len(temp)):
    ans -= sum(list(map(int, temp[i].split('+'))))
print(ans)
```

