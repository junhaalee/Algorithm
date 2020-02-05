from collections import deque

T = int(input())

for _ in range(T):
    T = True

    p = list(input())
    n = int(input())
    try:
        temp = deque(list(map(int, list(input().replace('[','').replace(']','').split(',')))))
    except:
        pass

    for i in range(len(p)):

        if p[i] == 'R':
            temp = deque(list(temp)[::-1])
        else:
            try:
                temp.popleft()
            except:
                print('error')
                T = False
                break
    if T:
        print(list(temp))
