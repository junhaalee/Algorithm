### 백준  - [1780](https://www.acmicpc.net/problem/1780)

### 풀이

* 시간과 메모리를 최대한 줄일 수 있는 방법으로 코딩하자.
* 굳이 paper의 모든 숫자를 다 확인할 필요는 없다. 하나라도 다르다면 바로 break.

```Python
check = paper[x][y]

TF = 0

for i in range(x,x+k):
    for j in range(y,y+k):
        if check != paper[i][j]:
            TF = 1
            break
```

