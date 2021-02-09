### LeetCode - [Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)

### 풀이

* 분할정복 = 재귀
* 재귀 = 어려움
* 분할정복 = 어려움

```Python

class Solution:
    def diffWaysToCompute(self, input: str):

        def compute(left, right, op):
            result = []
            for l in left:
                for r in right:
                    result.append(eval(str(l)+op+str(r)))
            return result

        if input.isdigit():
            return [int(input)]

        result = []

        for index, value in enumerate(input):
            if value in '*+-':
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index+1:])

                result.extend(compute(left,right,value))

        return result

```

