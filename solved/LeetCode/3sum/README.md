### LeetCode - [3 Sum](https://leetcode.com/problems/3sum)

### 풀이

* 

```Python

# 1. 나의 풀이 - 시간 초과
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        ans = []
        nums.sort()

        for i in range(len(nums)):

            left, right = i+1, len(nums)-1
            
            while left < right:
                
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                
                else:
                    temp = [nums[i],nums[left],nums[right]]
                    
                    if temp not in ans:
                        ans.append(temp)
                    
                    left += 1
                    right = len(nums)-1

        return ans



# 2. 나의 풀이 + 중복 처리 - 6352ms / 17.6MB
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        ans = []
        nums.sort()

        for i in range(len(nums)):
            
            # nums에 중복된 값이 있을 수 있으므로, 그럴 경우 continue로 건너뛰어 버리기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            
            while left < right:
                
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                
                else:
                    temp = [nums[i],nums[left],nums[right]]
                    
                    if temp not in ans:
                        ans.append(temp)
                    
                    left += 1
                    right = len(nums)-1

        return ans



# 3. 또 다른 투 포인터 - 856ms / 17.6MB
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        ans = []
        nums.sort()

        for i in range(len(nums)):
            
            # nums에 중복된 값이 있을 수 있으므로, 그럴 경우 continue로 건너뛰어 버리기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            
            while left < right:

                sum = nums[i] + nums[left] + nums[right]
                
                if sum < 0:
                    left += 1
                
                elif sum > 0:
                    right -= 1
                
                else:
                    # sum = 0 인 경우, 정답 및 스킵 처리
                    ans.append([nums[i],nums[left],nums[right]])
                    
                    # 같은 숫자가 연속으로 있을 경우 중복 처리
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    while left<right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return ans
```
* 문제의 특성에 맞는 조건 처리 필요 - 시간을 엄청나게 줄일 수 있음
* 이 문제 같은 경우는 다른 투 포인터와 다르게, 정답 처리 이후에 left, right가 동시에 움직임 -> sum이 0이여야 하는 특성 때문에 하나의 포인터만 움직이는 경우는 의미가 없음
