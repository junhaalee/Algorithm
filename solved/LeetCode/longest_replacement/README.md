### LeetCode - [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

### 풀이

* 슬라이딩 윈도우 + 투포인터

```Python

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = right = 0
        cnt = Counter()

        for right in range(1,len(s)+1):
            cnt[s[right-1]] += 1
            # 가장 많이 출현한 알파벳의 개수
            v = cnt.most_common(1)[0][1]

            # k보다 변경해야할 알파벳의 개수가 더 많다면
            # left += 1
            if right - left - v > k:
                left += 1
                cnt[s[left]] -= 1
            
            # max_len 갱신
            max_len = max(max_len,right-left)

        return max_len



```

