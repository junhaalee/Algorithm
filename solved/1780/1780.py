import sys
input = sys.stdin.readline

n = int(input())

paper = []

for _ in range(n):
    paper.append(list(map(int, input().split())))

def sol(x,y,k,ans):

    check = paper[x][y]

    TF = 0

    for i in range(x,x+k):
        for j in range(y,y+k):
            if check != paper[i][j]:
                TF = 1
                break

    if TF == 1:
        for i in range(3):
            for j in range(3):
                sol(x+k//3*i,y+k//3*j,k//3,ans)

    else:
        ans[check] += 1

    return ans

temp = sol(0,0,n,[0,0,0])

for i in range(-1,2):
    print(temp[i])