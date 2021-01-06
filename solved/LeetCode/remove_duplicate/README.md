### LeetCode - [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

### 풀이

* Python은 stack인 동시에 list이기도 하니깐 이것을 잘 활용하면 코드가 깔끔해진다

```Python

# 1. Stack 풀이
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # seen : 이미 처리된 문자 여부 확인용
        stack, seen, counter = [], set(), Counter(s)

        for char in s:
            
            counter[char] -= 1
            
            if char in seen:
                continue
            # stack에 있는 문자들이 char보다 사전상 뒤에 오는 문자이고, 뒤에 또 있는 문자인데 stack에 있을 경우 제거
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)

        return ''.join(stack)

# 2. Stack 풀이 2
# Python의 stack은 list로 활용이 가능하고, list는 in이라는 탐색기능을 제공하기 때문에 가능한 풀이
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, counter = [], Counter(s)

        for char in s:
            
            counter[char] -= 1
            
            if char in stack:
                continue

            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                stack.pop()

            stack.append(char)
        
        return ''.join(stack)


# 3. 재귀 - 이해가 불가능
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char,''))
        return ''
```
