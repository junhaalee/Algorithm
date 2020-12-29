### 백준  - [1697](https://www.acmicpc.net/problem/1697)

### 풀이

* 5등이다. 좀 뿌듯하다.
* 앞에서부터 찾아가는 방법도 좋지만, 때로는 뒤에서부터 훑어내려오는 방법도 좋다.

```Python
if t%2 == 0 and dp[t//2] == 0:
    dp[t//2] = count
    arr.append(t//2)
```

