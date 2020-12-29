### 백준  - [1931](https://www.acmicpc.net/problem/1931)

### 풀이

* 시간표 정렬이 핵심. [시작 시간 기준으로 정렬 -> 종료 시간 기준으로 정렬] 하던지, 반대로 하던지.
* 시작 시간과 종료 시간 모두 신경을 써주어야 함.

```Python
time = sorted([list(map(int, input().split())) for _ in range(int(input()))],key = lambda x : (x[1],x[0]))

result = [time[0]]

for i in range(1, len(time)):
    if time[i][0] >= result[-1][1]:
        result.append(time[i])

print(len(result))
```
