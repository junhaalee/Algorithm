### 백준  - [1904](https://www.acmicpc.net/problem/1904)

### 풀이

* 규칙을 찾는 연습을 하자

```Python
n = int(input())

ans = [1,2]

for i in range(2, n):
    ans.insert(i,ans[i-1]%15746+ans[i-2]%15746)

print(ans[-1]%15746)
```

