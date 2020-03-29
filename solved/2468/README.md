### 백준  - [2468](https://www.acmicpc.net/problem/2468)

### 풀이

* 이제까지 DFS를 이용할 때, 한번 방문했던 곳에 대한 설정을 graph의 값을 바꾸는 식으로 했는데, 이 문제에서는 visit이라는 matrix를 만들어서 표시를 하도록 했다. 그러면 graph를 복사하지 않아도 된다.
* max를 생각보다 다양하게 활용할 수 있다.

```Python
### visit이라는 matrix 활용하기
visit = [[1]*n for _ in range(n)]

### max 활용
for k in range(max(map(max,graph))):
```

