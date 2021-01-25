from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = right = 0
        cnt = Counter()

        for right in range(1,len(s)+1):
            cnt[s[right-1]] += 1
            v = cnt.most_common(1)[0][1]

            if right - left - v > k:
                left += 1
                cnt[s[left]] -= 1
            
            max_len = max(max_len,right-left)

        return max_len

