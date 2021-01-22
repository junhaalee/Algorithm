matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for m in matrix:
            if (m[0] <= target <= m[-1]):
                index = bisect.bisect_left(m,target)
                if index < len(m) and m[index] == target:
                    return True
                    break
                    
        return False
        