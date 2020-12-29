### 백준  - [5014](https://www.acmicpc.net/problem/5014)

### 풀이

* 단순 배열 대신에 deque를 사용했더니, 시간이 많이 줄어들었다.
* deque의 어떤 특징 때문에 시간 감소 효과를 볼 수 있었던 것인지 기억하잣.

```Python
    queue = deque([(s, 0)]) 
    visit = [0] * (f+1) 
    visit[s] = 1
```

