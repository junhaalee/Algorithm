### 백준 - [5052](https://www.acmicpc.net/problem/5052)

### 풀이

* 문자열 배열을 정렬하면 사전순으로 정렬됨.

```Python

def sol(nums):
    # 사전순으로 정렬되기 때문에, 바로 다음 num과만 비교해주면됨. O(n)
    for i in range(len(nums)-1):
        if nums[i+1].startswith(nums[i]):
            return False
    return True

```

