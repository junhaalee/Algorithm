t = int(input())


# 재귀 - 시간초과
# def f(k, n):

#     if k <= 0:
#         return n
#     elif n == 1:
#         return 1

#     return f(k-1,n)+f(k, n-1)

# for i in range(t):
#     k = int(input())
#     n = int(input())
#     print(f(k,n))

# 반복문

for _ in range(t):
    k = int(input())
    n = int(input())
    h = [i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1, n):
            h[j] += h[j-1]
    
    print(h[-1])

