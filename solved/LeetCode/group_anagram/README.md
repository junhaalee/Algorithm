### LeetCode - [Group Anagrams](https://leetcode.com/problems/group-anagrams)

### 풀이

* dict의 value는 list도 가능
*
* sorted() : input - string, list 둘 다 가능 / output - list
* sort() : input(?) - list / output - None
*
* defaultdict
* 존재하지 않는 키를 조회할 경우, 에러 메시지를 출력하는 대신 디폴트 값을 기준으로 해당 키에 대한 딕셔러니 아이템 생성
* value의 기본값을 미리 설정할 수 있음
* int -> 0 / str -> '' / list -> []
* from collections import defaultdict
* dd = defaultdict(str)

```Python

# 나의 풀이 - 92ms / 17.2MB
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()

        # 각 단어 정렬
        for s in strs:
            temp = ''.join(sorted(list(s)))
            # key는 정렬된 단어 = value는 그 단어에 해당하는 str들의 list
            if temp in dic.keys():
                dic[temp].append(s)
            else:
                dic[temp] = [s]

        return list(dic.values())



# defaultdict 사용 - 92ms / 17.8MB
# 훨씬 간결함.
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    	# value의 기본값을 list로 설정.
        anagram = defaultdict(list)

        for s in strs:
            anagram[''.join(sorted(s))].append(s)
        
        return anagram.values()
```

