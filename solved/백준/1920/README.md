### 백준  - [1920](https://www.acmicpc.net/problem/1920)

### 풀이

* 이분탐색의 기본
* s : 시작 index
* e : 마지막 index
* x : 찾으려는 element

```Python
def search(x,s,e,arr):

    if s > e:
        return False

    mid = (s+e)//2

    if arr[mid] == x:
        return True
    elif arr[mid] > x:
        e = mid - 1
    else:
        s = mid + 1
```

