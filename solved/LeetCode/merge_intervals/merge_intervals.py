intervals = [[1,3],[2,6],[5,10],[15,18]]

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key = lambda x : x[0])

        ind = 0
        while ind < len(intervals)-1:
            if intervals[ind][1] >= intervals[ind+1][0]:
                intervals[ind] = [intervals[ind][0],max(intervals[ind+1][1],intervals[ind][1])]
                intervals.remove(intervals[ind+1])
            else:
                ind += 1
        
        return intervals