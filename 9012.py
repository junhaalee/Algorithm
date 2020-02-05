n = int(input())

test = []

for _ in range(n):
    test.append(input())

temp = '))'

def sol(temp):

    ans = []

    for i in range(len(temp)):
        if temp[i] == '(':
            ans.append(temp[i])
        else:
            try:
                if ans[-1] == '(':
                    ans.pop()
            except:
                ans.append(temp[i])

    if len(ans) == 0:
        print('YES')
    else:
        print('NO')

for i in range(n):
    sol(test[i])
