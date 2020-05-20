### 백준  - [1100](https://www.acmicpc.net/problem/1100)

### 풀이

* 배열 복사 
* a = [1,2,3,4,5,6] 일때, b = a[::2]하면 b = [1,3,5]이고, b = a[1::2]하면 b = [2,4,6]

* 배열 count
* a = [1,2,3,2,1] 일때, a.count(2)하면 2

* 알면 활용하자. 

```Python
    if count%2:
        ans += temp[::2].count('F')

    else:
        ans += temp[1::2].count('F')
```

