### 백준  - [2178](https://www.acmicpc.net/problem/2178)

### 풀이

* visit을 그때 그때 update 해주어도 상관없는 문제였음 - 경로가 상관없을 때에는 저장다하면 비효율적.

```Python
while(True):

    if [h-1,w-1] in visit:
        break

    temp = []
    for p in visit:
        for k in range(4):
            tx = p[0] + dx[k]
            ty = p[1] + dy[k]
            if tx>=0 and ty>=0 and tx<h and ty <w and graph[tx][ty]:
                temp.append([tx,ty])
                graph[tx][ty] = 0
    
    visit = temp
    count += 1
```

