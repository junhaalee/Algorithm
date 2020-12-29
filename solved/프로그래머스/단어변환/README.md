### 백준  - [ ](https://www.acmicpc.net/problem/)

### 풀이

* DFS는 스택 또는 재귀 / BFS는 큐

```Python

        while True:

            if target in temp:
                break

            for t in temp:
                arr = []
                for i in range(len(words)):
                    if len(words[i]) == len(begin) and dif(t, words[i]):
                        arr.append(words[i])
                        words[i] = ''
            temp = arr

            ind += 1

```

