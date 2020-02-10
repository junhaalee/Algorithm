### 백준  - [11729](https://www.acmicpc.net/problem/11729)

### 풀이

* 하노이의 탑 : n-1개의 원반은 1->3->2로 옮기고, n번째 원반을 1->2->3으로 옮긴 후에, 다시 n-1개의 원반을 2->1->3으로 옮기기

```Python
n = int(input())

def sol(n,a,b,c):

    if n == 1:
        print(a,c)
    else:
        sol(n-1,a,c,b)
        print(a,c)
        sol(n-1,b,a,c)

print(2**n-1)
sol(n,1,2,3)
```

