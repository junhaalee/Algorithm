### 프로그래머스 - [가장 먼 노드](https://programmers.co.kr/learn/courses/30/lessons/49189)

### 풀이

* 그래프 활용
* deque를 활용한 BFS

```Python

#시간초과
def solution(n, edge):

    graph = [[0]*(n+1) for _ in range(n+1)]

    for e in edge:
        graph[e[0]][e[1]] = 1
        graph[e[1]][e[0]] = 1

    record = [0]*(n+1)

    current = 1

    visit = [current]
    queue = [current]

    count = 1

    while queue:
        temp = []

        for current in queue:

            if record[current] == 0:
                record[current] = count
                    
            for next in range(len(graph[current])):
                if graph[current][next] and next not in visit:
                    visit.append(next)
                    temp.append(next)

        queue = temp
        count += 1

    return record.count(max(record))

#deque 이용
from collections import deque

def bfs(current, record, graph):

    count = 1

    deq = deque([[current,count]])

    while deq:

        value = deq.popleft()
        current,count = value[0],value[1]

        if record[current] == 0:
            record[current] = count
            count += 1
            for next in graph[current]:
                deq.append([next,count])


def solution(n, edge):

    record = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    bfs(1,record,graph)

    return record.count(max(record))

```

