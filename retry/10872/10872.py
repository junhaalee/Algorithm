n = int(input())

def sol(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*sol(n-1)

print(sol(n))