### 백준  - [9095](https://www.acmicpc.net/problem/9095)

### 풀이

* 프로그래머스의 타겟 넘버와 비슷한 문제
* 1,2,3을 더해가면서 해당하는 숫자가 있으면, count.

```Python
elif ans[i] == n:
    count += 1
    ans.remove(ans[i])
```

