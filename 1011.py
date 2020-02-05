def p(n):
    if n <= 1:
        return 1
    else:
        return n+p(n-1)

def sol(k, n):
    
    ans = 2
    
    n = n-k-1
    k = 1

    i = 1

    while(True):
        if p(i) >= n-k:
            break
        else:
            k += i
            i += 1

    return ans+i

t = int(input())

for _ in range(t):
    k, n = map(int, input().split())
    print(sol(k,n))

