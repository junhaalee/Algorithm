### 백준  - [1966](https://www.acmicpc.net/problem/1966)

### 풀이

* 알고있는데 활용하지 못한다면, 그건 모르는거다.

```Python
        if loc != 0:
            if deq[0] == max(deq):
                temp.append(deq.popleft())
            else:
                deq.rotate(-1)
            loc -= 1
        else:
            if deq[0] == max(deq):
                break
            else:
                deq.rotate(-1)
                loc = len(deq)-1
```

