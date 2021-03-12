### 백준 - [1644](https://www.acmicpc.net/problem/1644)

### 풀이

* 에라토스테네스의 체 - 소수를 찾는 방법
* 2부터 소수를 구하고자 하는 구간의 모든 수를 나열, 자기 자신을 제외한 2의 배수를 모두 지운다
* 남아있는 수 가운데 3은 소수이므로, 자기 자신을 제외한 3의 배수를 모두 지운다 --> 계속 반복
* 참고 : https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4

* if / else만 잘써도 시간이 많이 줄어든다.

```Python

# 에라토스테네스의 체
def primes(n):
    
    # 소수는 2부터니깐 result[2]부터는 일단 모두 소수라고 가정
    result = [False,False] + [True]*(n-1)
    
    # 2부터 배수들 지우기
    for i in range(2, int(n**0.5+1)):
        if result[i]:
            result[2*i::i] = [False]*((n-i)//i)
    
    # True로 남아있는 수들만 모으기
    return [x for x in range(n+1) if result[x]]


# 780ms
while right < len(nums) and left <= right:

    s = sum(nums[left:right+1]) 

    if s < n:
        right += 1

    elif s == n:
        answer += 1
        right += 1
    
    else:
        left += 1

# 5300ms
while right < len(nums) and left <= right:

    s = sum(nums[left:right+1]) 

    if s < n:
        right += 1

    else:
        if s == n:
            answer += 1
        right += 1
        left += 1
```

