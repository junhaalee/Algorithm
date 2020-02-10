n = int(input())

def sol(n,a,b,c):

    if n == 1:
        print(a,c)
    else:
        sol(n-1,a,c,b)
        print(a,c)
        sol(n-1,b,a,c)

print(2**n-1)
sol(n,1,2,3)