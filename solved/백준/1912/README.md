### 백준 - [1912](https://www.acmicpc.net/problem/1912)

### 풀이

* 카데인 알고리즘
* 부분 수열의 합을 O(n)으로 구할 수 있는 알고리즘

```Python
for num in nums:
    current = max(num, current+num)
    best = max(best, current)
```

* current
* 현시점(nums의 각 element)까지의 최고합
* current까지의 합이 더 높은지 current부터 시작하는 합이 더 높은지 판단해서 max 선택
*
* best
* 부분 수열의 합 중 최고합
* 새로 갱신된 current와 best를 비교해서 max 선택