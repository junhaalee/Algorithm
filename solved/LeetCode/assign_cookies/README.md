### LeetCode - [Assign Cookies](https://leetcode.com/problems/assign-cookies/)

### 풀이

* O(n)에 가능

```Python

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child = cookie = 0

        while child < len(g) and cookie < len(s):
            # child에게 cookie 할당되면 다음 child로
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        
        return child
```

