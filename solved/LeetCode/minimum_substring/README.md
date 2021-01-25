### LeetCode - [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

### 풀이

* 어렵다
* Counter와 조합으로 O(n)에 가능

```Python

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)

        left = start = end = 0
        
        # right 포인터 오른쪽으로 이동
        for right, char in enumerate(s,1):
            missing -= need[char] > 0
            need[char] -= 1

            # right 포인터 증가시키다가 missing이 0이되면
            if missing == 0:
                # left 포인터를 증가시키기
                # need의 value가 음수라는 말은 left:right 범위안에 같은 문자가 두번 이상 있다는 의미
                while left < right and need[s[left]] < 0:
                    left += 1
                    need[s[left]] += 1
                # start:end 갱신
                if not end or right - left <= end - start:
                    start, end = left, right
                # 또 다른 left:right를 찾아서
                need[s[left]] += 1
                missing += 1
                left += 1
        
        return s[start:end]
                
```

