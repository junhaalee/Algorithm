### 백준  - [17836](https://www.acmicpc.net/problem/17836)

### 풀이

* 최대한 다양한 테스트 케이스에 대해서 생각하는 습관을 가져야 한다.

```Python
count = min(count, check_count+(n+m-2)-sw[0]-sw[1]) if check else count
```

