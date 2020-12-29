### LeetCode - [Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/)

### 풀이

* isdigit() : 문자열에 대해서 숫자 여부를 판별하는 함수

```Python

# 나의 풀이
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let, dig = [],[]
        for l in logs:
            if l.split()[1].isdigit():
                dig.append(l)
            else:
                let.append(l)

        let = sorted(let, key = lambda x : (x.split()[1:], x.split()[0]))
        
        return let+dig

```