s = 'ADOBECODEBANC'
t = 'ABC'

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)

        left = start = end = 0

        for right, char in enumerate(s,1):
            missing -= need[char] > 0
            need[char] -= 1

            if missing == 0:
                print(left, right)
                while left < right and need[s[left]] < 0:
                    left += 1
                    need[s[left]] += 1
                if not end or right - left <= end - start:
                    start, end = left, right
                
                need[s[left]] += 1
                missing += 1
                left += 1
        
        return s[start:end]
                