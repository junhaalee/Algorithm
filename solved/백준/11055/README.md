### 백준  - [11055](https://www.acmicpc.net/problem/11055)

### 풀이

* 다양한 테스크 케이스에 대해서 생각해보자.
* LIS(Longest Increasing Sequence)와 비슷한 문제였다. Longest를 Biggest로 생각하면 쉬운 문제.

```Python
for i in range(1,n):
    for j in range(i):
        if nums[j] < nums[i]:
            result[i] = max(result[i],result[j]+nums[i])
```

