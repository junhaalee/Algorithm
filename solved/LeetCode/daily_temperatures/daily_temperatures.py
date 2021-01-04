T = [73,74,75,71,69,72,76,73]

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        ans = [0]*len(T)
        stack = []

        for i,temp in enumerate(T):

            while stack and T[stack[-1]] < T[i]:
                last = stack.pop()
                ans[last] = i - last

            stack.append(i)        
        
        return ans