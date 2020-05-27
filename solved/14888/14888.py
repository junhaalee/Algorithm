import sys
from itertools import permutations
input = sys.stdin.readline


n = int(input())
nums = list(map(int, input().split()))[::-1]

cal = list(map(int, input().split()))

op = []

for ind in range(len(cal)):
    if ind == 0:
        for _ in range(cal[ind]):
            op.append('+')
    elif ind == 1:
        for _ in range(cal[ind]):
            op.append('-')
    elif ind == 2:
        for _ in range(cal[ind]):
            op.append('*')
    elif ind == 3:
        for _ in range(cal[ind]):
            op.append('//')

ops = list(permutations(op,len(op)))

ans = []

for op in ops:
    num = nums[::]
    ind = 0
    while(True):

        if len(num) == 1:
            break

        a = num.pop()
        b = num.pop()

        if op[ind] == '+':
            num.append(a+b)
        elif op[ind] == '-':
            num.append(a-b)
        elif op[ind] == '*':
            num.append(a*b)
        elif op[ind] == '//':
            num.append(0) if abs(a) < abs(b) else num.append(a//b)

        ind += 1
    ans.append(num[0])

print(max(ans))
print(min(ans))