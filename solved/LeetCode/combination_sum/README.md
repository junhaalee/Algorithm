### LeetCode - [Combination Sum](https://leetcode.com/problems/combination-sum/)

### 풀이

* 

```Python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []

        # csum : target가 비교하는 변수
        # path : csum을 구성하는 원소들
        # index : 가장 최근에 path에 추가된 원소의 위치
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 만약 순열 문제였다면, index부터 len(candidates)가 아니라 0부터 len(candidates) 탐색으로 했으면 가능
            for i in range(index, len(candidates)):
                dfs(csum-candidates[i], i, path+[candidates[i]])
        
        dfs(target,0,[])
        
        return result

```