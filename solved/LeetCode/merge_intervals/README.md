### LeetCode - [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

### 풀이

* 

```Python

# 1. 내 풀이
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key = lambda x : x[0])

        ind = 0
        while ind < len(intervals)-1:
            if intervals[ind][1] >= intervals[ind+1][0]:
                # intervals[ind][1]이 intervals[ind+1][1]보다 클 수도 있음
                intervals[ind] = [intervals[ind][0],max(intervals[ind+1][1],intervals[ind][1])]
                intervals.remove(intervals[ind+1])
            else:
                ind += 1
        
        return intervals


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge = []
        for i in sorted(intervals, key = lambda x : x[0]):
            if merge and i[0] <= merge[-1][1]:
                merge[-1][1] = max(merge[-1][1],i[1])
            else:
                # 중첩 리스트로 만들어주는 역할
                # merge += [i]와 똑같음
                merge += i,
        
        return merge

```