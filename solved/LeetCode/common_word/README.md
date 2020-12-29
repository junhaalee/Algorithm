### LeetCode - [Most Common Word](https://leetcode.com/problems/most-common-word/)

### 풀이

* re.sub(조건, 문자열2, 문자열1) : 문자열1에 대해서 조건에 만족하는 문자를 문자열2로 대체
* most_common(num) : 가장 빈도가 높은 상위 num개의 items()를 return

```Python

# 나의 풀이 - 36ms / 14.1MB
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        p = re.sub('[^\w]',' ',paragraph.lower())
        temp = p.split()
        
        cnt = dict(Counter(temp))
        for b in banned:
            try:
                del cnt[b]
            except:
                pass
        
        cnt = sorted(cnt.items(), key = lambda x : x[1], reverse = True)

        return cnt[0][0]


# Counter의 most_common 사용 - 24ms / 14.4MB
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        #banned에 포함되는 단어는 애초에 저장부터 안함
        words = [word for word in re.sub('[^\w]',' ',paragraph).lower().split()
                    if word not in banned]
        
        #most_common
        cnt = Counter(words)

        return cnt.most_common(1)[0][0]
```

