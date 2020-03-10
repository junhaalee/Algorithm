### 백준  - [1011](https://www.acmicpc.net/problem/1011)

### 풀이

* 규칙을 찾자.

```Python
for _ in range(int(input())):
    x,y = map(int, input().split())
    num = y-x
    i,k = 1,1
    
    while(num>0):
        num -= k
        k += 1
        if num >= i:
            num -= i
            i += 1
    
    print(k+i-2)
```

