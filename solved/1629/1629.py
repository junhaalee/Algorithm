import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

def sol(a,b,c):

    a = a%c
    if b <= 2:
        if b == 2:
            return a**2
        else:
            return a
    else:
        if b%2 == 0:
            return (sol(a,b//2,c)**2)%c
        else:
            return (a*sol(a,b//2,c)**2)%c