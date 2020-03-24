### 백준  - [11048](https://www.acmicpc.net/problem/11048)

### 풀이

* BFS와 DP 혼합 사용
* 약간 단계 단계 퍼져나가는 행위가 중요할 때에는 BFS를 사용하면 좋은 것 같다.

```Python
for x in range(n):
    for y in range(m):
        if x+y:
            temp = []
            for i in range(3):
                tx = x - dx[i]
                ty = y - dy[i]
                if tx >= 0 and ty >= 0 and tx < n and ty < m:
                    temp.append(graph[tx][ty])
            graph[x][y] += max(temp)
```

