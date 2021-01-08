s = 'abcabcbb'
s = 'pwwkew'

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left,right = 0,0

        while s and right < len(s):

            tmp = s[left:right+1]

            if len(tmp) == len(set(tmp)):
                right += 1
                ans = max(ans, len(tmp))
            else:
                left += 1

        return ans



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = max = 0

        for index, char in enumerate(s):

            if char in used and used[char] >= start:
                start = used[char] + 1
            else:
                max = max(max, index-start+1)
        
            used[char] = index
        
        return max