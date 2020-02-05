from collections import deque

temp = deque()

n = int(input())

for _ in range(n):

    T = input()

    f = T.split()[0]

    try:

        if f == "push_back":
            temp.append(T.split()[1])
        
        elif f == "push_front":
            temp.appendleft(T.split()[1])

        elif f == "pop_front":
            print(temp.popleft())

        elif f == "pop_back":
            print(temp.pop())


        elif f == "size":
            print(len(temp))

        elif f == "empty":
            if len(temp) == 0 : print(1)
            else: print(0)

        elif f == "front":
            print(temp[0])


        elif f == "back":
            print(temp[-1])
            
    except:
        print(-1)
