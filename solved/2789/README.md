### 백준  - [2789](https://www.acmicpc.net/problem/2789)

### 풀이

* 2가지 풀이 방법이 있다.
* 1. CAMBRIDGE에 있는 알파벳을 제거하는 방법 - 반복문 2번
* 2. CAMBRIDGE에 없는 단어를 추가하는 방법 - 반복문 1

* 나는 1번 방법을 사용하였는데, 2번 방법의 처리 속도가 빠르다. 

```Python
#2번 방법
s = input()
cam = "CAMBRIDGE"

result = ""
for c in s:
    if c not in cam:
        result += c

print(result)
```

