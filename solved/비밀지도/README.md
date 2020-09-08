### 백준  - [ ](https://www.acmicpc.net/problem/)

### 풀이

* bin(n) : int형 변수를 이진수로 변환해주는 함수.
* | : 비트 연산자 - or
* 두 배열을 비교할 때는 zip을 사용해보자

```Python
#다른 사람의 풀이 - 비트 연산자 사용

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer


```

