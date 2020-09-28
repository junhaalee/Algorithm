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
