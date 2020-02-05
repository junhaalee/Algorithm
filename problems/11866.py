from collections import deque

n, k = map(int, input().split())

temp = deque([i for i in range(1, n+1)])
ans = []

while(True):

    if len(temp) == 0:
        break

    temp.rotate(-(k-1))
    ans.append(temp.popleft())

print('<'+', '.join(map(str, ans))+'>')