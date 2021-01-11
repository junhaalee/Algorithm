digits = '23'

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

        stack = ['']

        for dig in digits:
            temp = []
            while stack:
                s = stack.pop()
                for i in range(len(dic[dig])):
                    temp.append(s+dic[dig][i])
            stack = temp
            
        return stack
            


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dfs(0,'')
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

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
