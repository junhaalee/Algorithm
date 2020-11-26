### 백준 - [수들의합2](https://www.acmicpc.net/problem/2003)

### 풀이

* 투 포인터 알고리즘
* '1차원 배열이 있을 때, 부분 배열 중 그 원소 합이 M이 되는 경우의 수를 구하여라'라는 경우 사용 --> O(n)으로 쌉가능
* 포인터 2개 s,e = 0,0
* sum(배열[s:e])이 M보다 작을 경우, e++
* sum(배열[s:e])이 M보다 클 경우, s++
* sum(배열[s:e])이 M일 경우, s++ and e=s

```Python
s,e = 0,0
while s<=e and e<=len(nums):
    if sum(nums[s:e]) < M:
        e += 1
    elif sum(nums[s:e]) > M:
        s += 1
    else:
        ans += 1
        s += 1
        e = s
```

