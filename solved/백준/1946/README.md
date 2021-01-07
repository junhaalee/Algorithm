### 백준 - [1946](https://www.acmicpc.net/problem/1946)

### 풀이

* LeetCode의 https://leetcode.com/problems/daily-temperatures/ 와 굉장히 비슷
* 기준을 만족하지 않을 경우, stack에서 pop

```Python
# nums는 (key = lambda x : x[0])을 기준으로 정렬한 상태
# 즉, 이미 num[0]은 다음 num[0]보다 순위에서 밀리므로
# num[1]까지 순위가 밀리면 pop
for num in nums:
    while stack and stack[-1][1] > num[1]:
            stack.pop()
    stack.append(num)
```

