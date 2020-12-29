from collections import deque

for _ in range(int(input())):

    n,loc = map(int, input().split())
    deq = deque(list(map(int, input().split())))
    
    temp = []
    while(True):

        if len(deq) == 0 :
            break

        if loc != 0:
            if deq[0] == max(deq):
                temp.append(deq.popleft())
            else:
                deq.rotate(-1)
            loc -= 1
        else:
            if deq[0] == max(deq):
                break
            else:
                deq.rotate(-1)
                loc = len(deq)-1

    print(len(temp)+1)