### LeetCode - [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)

### 풀이

* 투 포인터를 이용하면 O(n^2)-> O(n)

```Python

# 1. 투 포인터
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        # 최대 높이의 막대까지 각각 좌우 기둥 최대 높이 left_max, right_max가 현재 높이와의 차이만큼 물 높이 volumeㅇ르 더해 나간다.
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            
            # left_max, right_max가 한 칸씩 전진하면서 height[left],height[right]과의 차이를 더해가는 방식
            left_max = max(height[left],left_max)
            right_max = max(height[right], right_max)
            
            # 가장 높이가 높은 막대에서 좌우 포이너가 서로 만나게 됨 - O(n)
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        
        return volume


# 2. 스택
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]])-height[top]

                volume += distance * waters

            stack.append(i)
            
        return volume
```
* 스택은 이해가 잘 안됨 - 다시 확인
* O(n^2)-> O(n) 되도록 최대한 생각해보기
