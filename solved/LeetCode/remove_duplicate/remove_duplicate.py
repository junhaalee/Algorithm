s = 'cbacdcbc'

from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, seen, counter = [], set(), Counter(s)

        for char in s:
            
            counter[char] -= 1
            
            if char in seen:
                continue

            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)

        return ''.join(stack)

solution = Solution()
solution.removeDuplicateLetters(s)