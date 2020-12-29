def check(i):
    for j in range(0,i):
        if row[j] == row[i] or abs(row[j]-row[i]) == (i-j):
            return False
    return True
 
def sol(i):
    global result
    if i == N:
        result += 1
    else:
        for j in range(N):
            row[i] = j
            if check(i):
                sol(i+1)

N = int(input())
row = [0]*15
result = 0
sol(0)
print(result)
