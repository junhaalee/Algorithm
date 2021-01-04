s = "[()]"

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

sol = Solution()
sol.isValid(s)