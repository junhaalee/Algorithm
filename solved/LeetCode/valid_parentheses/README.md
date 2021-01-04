### LeetCode - [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

### 풀이

* 스택 기본 문제

```Python
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '[':']', '{':'}'}
        stack = []

        for p in s:
            if p in dic:
                stack.append(p)
            elif not stack or dic[stack.pop()] != p:
                return False
        
        return len(stack) == 0
```
* return (조건)일 경우, 조건이 참일 경우는 True를 거짓일 경우는 False를 반환
