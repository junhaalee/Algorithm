nums = [1,1,1,2,2,3]
k = 2

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [s[0] for s in Counter(nums).most_common(k)]

