from collections import deque

temp = deque([a for a in range(1,int(input())+1)])

while(True):

    if len(temp) == 1:
        break

    temp.popleft()
    temp.rotate(-1)

print(temp[0])