import sys
input = sys.stdin.readline

paper = []
n = int(input())
for _ in range(n):
    paper.append(list(map(int, input().split())))

def sol(x,y,k,ans):

    check = 0

    for i in range(x, x+k):
        for j in range(y, y+k):
            check += paper[i][j]
    
    if check == 0:
        ans[0]+= 1
    elif check == k*k:
        ans[1]+= 1

    else:
        sol(x+k//2,y,k//2,ans)
        sol(x,y+k//2,k//2,ans)
        sol(x+k//2,y+k//2,k//2,ans)
        sol(x,y,k//2,ans)
    
    return ans

for a in sol(0,0,n,[0,0]):
    print(a)