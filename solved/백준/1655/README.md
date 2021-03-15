### 백준  - [1655](https://www.acmicpc.net/problem/1655)

### 풀이

* 처음에는 이분 탐색으로 index를 찾아서 넣어주고 가운데 값을 출력했지만 - 시간초과
* 이유는 모르겠지만, list를 heappush하는 것보다 tuple을 넣어주는것이 시간 더 단축됨

* tuple과 list
* 공통점 : index 사용 가능
* 다른점 : 수정 불가능

```Python
# left와 right를 모두 이용하여 가운데 값 찾기

if len(left) == len(right):
    heappush(left, (-n,n))
else:
    heappush(right, (n,n))

# left[0][1]은 무조건 right[0][1]보다 작아야 하므로.
if right and left[0][1] > right[0][1]:
    l = heappop(left)[1]
    r = heappop(right)[1]

    heappush(left, (-r,r))
    heappush(right, (l,l))
```

