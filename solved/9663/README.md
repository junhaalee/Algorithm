### 백준  - [9663](https://www.acmicpc.net/problem/9663)

### 풀이

* row 별로 검사를 해 나가는 방식 - 같은 행이거나 또는 대각선 상에 있을 때 바로 제외해버리기.

```Python
def check(i):
    for j in range(0,i):
        if row[j] == row[i] or abs(row[j]-row[i]) == (i-j):
            return False
    return True
```

