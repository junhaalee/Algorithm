### 백준 - [1654](https://www.acmicpc.net/problem/1654)

### 풀이

* 이분탐색 활용. 단, 문제를 잘 읽고, start를 처음에 0으로 설정할지 1로 설정할지 정해야 한다.

```Python
start, finish = 0, max(length)

while(start <= finish):

    target = (start+finish)//2

    temp = 0
    for l in length:
        temp += l//target
    
    if temp < n:
        finish = target - 1
    else:
        start = target + 1

print(finish)
```

