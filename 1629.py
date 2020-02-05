A,B,C = map(int, input().split())


def cal(a,b):
    return a**b

def sol(A,B,C):

    ans = 0

    if B%2 == 0:
        ans =  cal(A,B//2)
    else:
        ans =  A * cal(A,(B-1)//2)

    print(ans%C)

sol(A,B,C)