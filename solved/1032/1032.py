import sys
input = sys.stdin.readline

n = int(input())

order = [input() for _ in range(n)]

if len(order) == 1:
    print(order[0])
else:

    ans = ''

    for i in range(len(order[0])):
        s = order[0][i]
        check = True
        k = 0
        while True:
            if k == n:
                break
            elif s != order[k][i]:
                check = False
                break
            k+=1
        ans = ans+order[0][i] if check else ans+'?'
    print(ans)