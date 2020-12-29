### LeetCode - [Longest Palindrome Substring](https://leetcode.com/problems/longest-palindromic-substring/)

### 풀이

* Longes Common Substring과 비슷한 문제. DP는 생각보다 빠르지 않음.


```Python

# 나의 풀이 - 시간 초과
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #답은 최소 한글자 이상
        ans = s[0]
        
        for i in range(len(s)+1):
            for k in range(i+1,len(s)+1):
                if s[i:k] == s[i:k][::-1]:
                    ans = s[i:k] if len(s[i:k])>len(ans) else ans

        return ans


# 중앙을 중심으로 확장하는 풀이 - 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1]
        
        # 해당 사항이 없을 땐 빠르게 return
        if len(s) < 2 or s == s[::-1]:
            return s

        ans = s[0]
        # i는 팰린드롬의 중심
        for i in range(len(s)-1):
            ans = max(ans, 
                        expand(i,i+1), # 홀수형 팰린드롬
                        expand(i,i+2), # 짝수형 팰린드롬
                        key = len)
        return ans
```

* i를 중심으로 s[left]와 s[right-1]를 비교해서 확장해나가는 방식 - 따라서 left, right-1만 유효한 범위 안에 있으면 됨(left >= 0, right-1 < len(s))

