### 백준  - [7576](https://www.acmicpc.net/problem/7576)

### 풀이

* 배열을 최소로만 이용해서 문제를 풀자.
* 처음에는 0의 위치를 저장하는 배열도 만들었지만, 없어도 상관없음을 너무 늦게 깨달았다.
* 1의 위치만 알아도 문제를 풀 수 있다.

```Python
graph = []
one = []
for i in range(h):
    temp = list(map(int, input().split()))
    for k in range(len(temp)):
        if temp[k] == 1 : one.append([i,k])
    graph.append(temp)
```

