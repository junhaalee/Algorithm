n = int(input())

def sol(n):
    if n == 0 or n == 1:
        return n
    else:
        return sol(n-1)+sol(n-2)

print(sol(n))