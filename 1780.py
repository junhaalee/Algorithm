n = int(input())

slice = []

for _ in range(n):
    slice.append(list(map(int, input().split())))

ans = [0,0,0]

def sol(x, y, k):

    global ans

    count = []

    for i in range(x, x+k):
        for j in range(y, y+k):
            count.append(slice[i][j])
    
    if len(set(count)) == 1:

        if list(set(count))[0] == -1:
            ans[0] += 1

        elif list(set(count))[0] == 0:
            ans[1] += 1

        elif list(set(count))[0] == 1:
            ans[2] += 1
        
    else:
        sol(x,y,k//3)
        sol(x+k//3,y,k//3)
        sol(x+k//3*2,y,k//3)

        sol(x,y+k//3,k//3)
        sol(x+k//3,y+k//3,k//3)
        sol(x+k//3*2,y+k//3,k//3)

        sol(x,y+k//3*2,k//3)
        sol(x+k//3,y+k//3*2,k//3)
        sol(x+k//3*2,y+k//3*2,k//3)

    return ans

ans = sol(0,0,n)

for i in range(3):
    print(ans[i])
    