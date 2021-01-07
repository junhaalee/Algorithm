import sys
input = sys.stdin.readline

for _ in range(int(input())):

    nums = [list(map(int, input().split())) for _ in range(int(input()))]

    nums = sorted(nums, key = lambda x : x[0], reverse = True)

    stack = []

    for num in nums:
        while stack and stack[-1][1] > num[1]:
                stack.pop()
        stack.append(num)

    print(len(stack))