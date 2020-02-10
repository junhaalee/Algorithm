### 백준  - [1018](https://www.acmicpc.net/problem/1018)

### 풀이

* 여러가지 방법이 있는 것 같은데, 결국에는 폭풍 for.

```Python
h, w = map(int, input().split())

chess = [input() for _ in range(h)]

ans = []

def sol(chess):

    case1 = ['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
    case2 = ['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
    
    if chess[0][0] == 'W':
        case = case1
    else:
        case = case2
    
    count = 0

    for i in range(8):
        for k in range(8):
            if chess[i][k] != case[i][k]:
                count += 1
    
    if count > 32:
        return (64-count)
    else:
        return count


for i in range(w-7):
    for k in range(h-7):
        val = []
        for j in range(k, k+8):
            val.append(chess[j][i:i+8])
        ans.append(sol(val))

print(min(ans))
```

