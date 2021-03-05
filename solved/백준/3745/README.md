### 백준 - [3745](https://www.acmicpc.net/problem/3745)

### 풀이

* 첫번째 풀이 - 카데인 알고리즘 비슷하게
* 두번째 풀이 - 이분 탐색

```Python

result = []

# 카데인 알고리즘 비슷하게 - 왜 틀리는지 도저히 모르겠다
def sol(nums):
    global result

    index, current = 0, 100001
    answer = 1

    for next_index, next in enumerate(nums):
        if current >= next:
            index = next_index
        answer = max(answer, next_index-index+1)
        current = next
        
    result.append(answer)

# 이분 탐색 - 통과
def sol2(nums):
    global result

    dp = [0]

    for num in nums:
        if num > dp[-1]:
            dp.append(num)
        else:
            dp[bisect.bisect_left(dp, num)] = num
    
    result.append(len(dp)-1)
        

```

