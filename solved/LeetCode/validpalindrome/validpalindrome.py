import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 소문자로 만들기
        s = s.lower()

        # 정규 표현식 활용하여 영문자, 숫자만 필터링
        s = re.sub('[^a-z0-9]','',s)

        return s == s[::-1]