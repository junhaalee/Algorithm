### LeetCode - [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

### 풀이

* max를 계산하는 부분에서의 최적화 차이

```Python
# 1. Brute Force - 시간 초과
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums)-k+1):
            print(nums[i:i+k])
            result.append(max(nums[i:i+k]))

# 2. Queue를 이용하는 방법
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_num = -sys.maxsize
        window = deque()

        for i,v in enumerate(nums):
            window.append(v)
            
            if i < k-1:
                continue
            
            # 새로운 값이 기존 max_num보다 더 클 때만 max_num 바꿔주기
            if max_num == -sys.maxsize:
                max_num = max(window)
            elif v > max_num:
                max_num = v
            
            result.append(max_num)

            # max_num이 window의 범위 안에 들어와있는지 확인
            # 범위 안에 없다면 다시 max_num 초기화
            if max_num == window.popleft():
                max_num = -sys.maxsize
        return result

```

