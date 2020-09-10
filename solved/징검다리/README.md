### 프로그래머스 - [징검다리 건너기](https://programmers.co.kr/learn/courses/30/lessons/64062)

### 풀이

* 이분탐색 활용

```Python

    while(left+1 < right):

        mid = (left+right)//2

        if check(stones, k, mid):
            left = mid
        else:
            right = mid


#비교 실험
import time
temp = [x for x in range(1000000)]
target = 621255

def bs(arr,target):

    left = arr[0]
    right = arr[-1]

    while(left+1 < right):

        mid = (left+right)//2

        if mid == target:
            break
        elif mid < target:
            left = mid+1
        else:
            right = mid -1

    return mid
    
start = time.time()

temp.index(target)
# bs(temp,target)

finish = time.time()

print(str(finish-start))

#index 함수를 이용 : 0.011148691177368164
#binary search : 0.001070261001586914

--> binary search가 훨씬 빠름

```

