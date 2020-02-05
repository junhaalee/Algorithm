
def sol(n):

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return sol(n-2)+sol(n-1)


n = int(input())
print(sol(n)) 