n = int(input())

def sol(n):
    if n == 0 or n == 1:
        return 1
    
    return sol(n-1)*n

print(sol(n))