### LeetCode - [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

### 풀이

* 내 풀이 : 스택을 이용한 반복 쌓기
* recursive DFS : 재귀를 이용한 반복 쌓기

```Python

# 1. 내 풀이 - 28ms / 14.4MB
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }

        if not digits:
            return []
        
        stack = ['']

        for dig in digits:
            temp = []
            while stack:
                s = stack.pop()
                for i in range(len(dic[dig])):
                    temp.append(s+dic[dig][i])
            stack = temp
            
        return stack


# 2. recursive DFS - 28ms / 14.4MB
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dfs(0,'')
        def dfs(index, path):
            # path가 완성되면 result에 추가
            if len(path) == len(digits):
                result.append(path)
                return

            # index는 글자 길이
            # path에 글자 추가
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)
            
        if not digits:
            return []
        
        dic = {'2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',}
        
        result = []
        dfs(0,'')

        return result     
```

