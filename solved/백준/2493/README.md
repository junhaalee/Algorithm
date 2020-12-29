### 백준  - [2493](https://www.acmicpc.net/problem/2493)

### 풀이

* stack 사용의 중요성
* stack에 길이가 긴 탑들을 저장해두고 비교하면서 진행
* 단순 반복문으로 사용하면 시간초과


```Python
for i in range(n-1):
    while stack :
        if stack[-1][1] > nums[i]:
            ans.append(stack[-1][0]+1)
            break
        stack.pop()

    if not stack:
        ans.append(0)
    stack.append([i,nums[i]])
```

