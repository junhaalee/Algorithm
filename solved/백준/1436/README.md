### 백준  - [1436](https://www.acmicpc.net/problem/1436)

### 풀이

* 딱히..

```Python
n = int(input())

ans = []

i = 1
while(True):

    if '666' in str(i):
        ans.append(i)
    
    if len(ans) == n:
        print(i)
        break
    
    i += 1
```


* 이런식으로 푼 사람들도 많았는데, 메모리는 내 풀이와 동일. 시간이 조금 빨라졌다. 시작점이 다르니.
```Python

N = int(input())
init = 666

while(N):
    if '666' in str(init):
        N -= 1
    
    init += 1
print(init - 1)
```
