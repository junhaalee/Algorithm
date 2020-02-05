n = int(input())

def sol(num1, num2, k):

    num = num1 + num2

    if k == n-1:
        return num
    else:
        return sol(num2, num, k+1)

if n <= 1:
    print(n)
else:
    print(sol(0,1,1))
    
