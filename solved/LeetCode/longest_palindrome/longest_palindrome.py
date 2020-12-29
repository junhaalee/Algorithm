class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right-1]:
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