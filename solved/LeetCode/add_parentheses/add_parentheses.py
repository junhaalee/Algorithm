class Solution:
    def diffWaysToCompute(self, input: str):
        def compute(left, right, op):
            print('left : '+str(left))
            print('right : '+str(right))
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
                print('result : ')
                print(result)
                print()
        
        return result

s = Solution()
input = '2*3-4*5'
print(s.diffWaysToCompute(input))