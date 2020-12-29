### 프로그래머스 - [입국심사](https://programmers.co.kr/learn/courses/30/lessons/43238)

### 풀이

* 이분탐색의 값과 기준 정하기
* 이분탐색 값 : 한 명의 심사관에게 얼마의 시간을 줄 것인가
* 이분탐색 기준 : 주어진 시간동안 각 심사관이 삼사를 했을 때, 심사를 마친 사람의 수

```Python

left = 0
right = n*max(times) #최악의 경우

if sum(temp) >= n:
    answer = mid 
    right = mid-1
else:
    left = mid+1	
```

