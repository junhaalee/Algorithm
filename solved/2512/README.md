### 백준 - [예산](https://www.acmicpc.net/problem/2512)

### 풀이

* right --> mid-1
* left --> mid+1
* ans --> mid

```Python

while left<=right:

    mid = (left+right)//2

    temp = sum([num if mid>=num else mid for num in nums])

    if temp>st:
        right = mid-1
    else:
        left = mid+1
        ans = mid
        
```

