### 백준 - [1806](https://www.acmicpc.net/problem/1806)

### 풀이

* 투 포인터
* 다른 문제와 다른 점은 left, right가 같은 곳에서 시작한다는 점.

```Python

while right < len(nums):

    if sum < s:
        right += 1
        if right < len(nums):
            sum += nums[right]
        
    else:
        ans = min(ans, right-left+1)
        sum -= nums[left]
        left += 1

```