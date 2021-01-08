### LeetCode - [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

### 풀이

* tmp라는 배열을 만들고 동적인 pointer도 두 개여서 시간이 오래 걸리는 것 같다

```Python

# 1. 내 풀이 : 투포인터 - 364ms / 14.5MB
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

# 2. dict를 활용한 풀이 - 56ms / 14.4MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = max_len = 0

        for index, char in enumerate(s):
            # char가 이미 사용됐다면, start 수정
            if char in used and used[char] >= start:
                # 사용됐던 위치 바로 다음부터 start
                start = used[char] + 1
            else:
                max_len = max(max_len, index-start+1)

            used[char] = index
        
        return max_len
```

