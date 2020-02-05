n = int(input())

slice = []

for _ in range(n):
    slice.append(list(map(int, input().split())))

def sol(x, y, k,ans):

    count = 0

    for i in range(x, x+k):
        for j in range(y, y+k):
            count += slice[i][j]
    
    if count == 0:
        ans[0] += 1

    elif count == k**2:
        ans[1] += 1
        
    else:
        sol(x,y,k//2,ans)
        sol(x+k//2,y,k//2,ans)
        sol(x,y+k//2,k//2,ans)
        sol(x+k//2,y+k//2,k//2,ans)
    
    return ans

for i in range(2):
    print(sol(0,0,n,[0,0])[i])