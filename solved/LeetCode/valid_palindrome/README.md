### LeetCode - [Valid Palindrome](https://leetcode.com/problems/valid-palindrome)

### 풀이

* 슬라이싱 - 문자열을 조작할 때는 항상 슬아이싱을 우선으로 사용하는 편이 속도 개선 유리.
* a.reverse() 하는 것보다 a[::-1]이 더 빠르다

```Python

# 나의 풀이 - 52ms / 20.5MB
from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        deq = deque([i.lower() for i in list(s) if i.isalnum()])
        temp = ''.join(deq)
        deq.reverse()

        if temp == ''.join(deq):
            return True
        else:
            return False

        return True if temp == ''.join(deq) else False


# 1. Deque를 이용한 또 다른 풀이 - 52ms / 20.3MB
from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        deq = deque([i.lower() for i in list(s) if i.isalnum()])
        
        while len(deq) > 1:
            if deq.pop() != deq.popleft():
                return False
        
        return True


# 2. 슬라이싱 & 정규표현식 사용 - 36ms / 15.7MB
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        return s == s[::-1]
```

