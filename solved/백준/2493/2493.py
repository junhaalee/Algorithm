n = int(input())
nums = list(map(int, input().split()))
stack = []
ans = []

for i in range(n-1):
    while stack :
        if stack[-1][1] > nums[i]:
            ans.append(stack[-1][0]+1)
            break
        stack.pop()

    if not stack:
        ans.append(0)
    stack.append([i,nums[i]])

print(' '.join(list(map(str,ans))))