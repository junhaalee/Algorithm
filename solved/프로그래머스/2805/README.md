### 백준 - [2805](https://www.acmicpc.net/problem/2805)

### 풀이

* 이분탐색 활용 - h를 이분탐색으로 찾기
* sum, max, min은 시간이 오래걸림

```Python

    while(left<=right):

        mid = (left+right)//2
        
        length = cut(trees,mid)

        if length >= m:
            left = mid+1
        else:
            right = mid-1

    print(right)

```

