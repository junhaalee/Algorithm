### LeetCode - [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

### 풀이

* 42. Trapping Rain Water 문제랑 유사
* 현재 인덱스를 계속 스택에 쌓아두다가, 이전보다 상승하는 지점에서 현대 온도와 스택에 쌓아둔 인덱스 지점의 돈도 차이 비교.
* stack에는 기준(기온이 높은 날을 만났을 때)을 만족하지 않는 날 저장 -> 기준 만족하면 pop

```Python
# 1. 내 풀이
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0]*len(T)
        stack = []

        for i in range(len(T)):

            while stack:
                if T[i] > T[stack[-1]]:
                    ans[stack[-1]] = i - stack[-1]
                    stack.pop()
                else:
                    break

            stack.append(i)
            
        return ans

# 2. Stack을 이용한 풀이
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        ans = [0]*len(T)
        stack = []

        for i,temp in enumerate(T):
            # 스택에 저장된 인덱스에 해당하는 온도와 현재 온도 비교
            while stack and T[stack[-1]] < T[i]:
                # 현재 온도가 더 높으면 pop
                last = stack.pop()
                # 현재 온도의 인덱스와 stack에 저장된 인덱스 차이 저장
                ans[last] = i - last

            stack.append(i)        
        
        return ans

```