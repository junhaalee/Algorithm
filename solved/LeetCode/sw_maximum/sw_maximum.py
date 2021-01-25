
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums)-k+1):
            print(nums[i:i+k])
            result.append(max(nums[i:i+k]))

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_num = -sys.maxsize
        window = deque()

        for i,v in enumerate(nums):
            window.append(v)
            
            if i < k-1:
                continue
                
            if max_num == -sys.maxsize:
                max_num = max(window)
            elif v > max_num:
                max_num = v
            
            result.append(max_num)

            if max_num == window.popleft():
                max_num = -sys.maxsize
        return result

s = Solution()

result = s.maxSlidingWindow([1,-1],1)
print(result)