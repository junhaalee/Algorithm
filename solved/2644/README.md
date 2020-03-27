### 백준  - [2644](https://www.acmicpc.net/problem/2644)

### 풀이

* DFS로 end가 그래프 안에 있는지 확인한 후에, 있다면 count를 하는 식으로 풀었다.
* 효율적인 코드는 아니지만, BFS와 DFS 모두 사용해볼 겸 풀어보았다.

```Python
check = dfs([],graph,start)
```

