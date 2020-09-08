### 프로그래머스 - [뉴스 클러스터링](https://programmers.co.kr/learn/courses/30/lessons/17677)

### 풀이

* 역시 정규표현식을 활용하면 좋다.

```Python
#내가 짠 코드
def word(s):
    
    result = []
    ind = 0
    while(ind < len(s)-1):

        if (64 < ord(s[ind].upper()) < 91) and (64 < ord(s[ind+1].upper()) < 91):
            temp = s[ind].upper()+s[ind+1].upper()
            result.append(temp)

        ind += 1
    
    return result


#정규표현식을 사용한 코드
def word(s):

    result = []
    s = s.upper()
    p = re.compile('[A-Z][A-Z]') # re.compile('[A-Z]{2}') 이것도 의미는 같음
    
    for i in range(len(s)-1):
        temp = s[i:i+2]
        if p.match(temp):
            result.append(temp)
    
    return result

```

