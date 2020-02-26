
n = int(input())
num = list(map(int, input().split()))

sol(num,0)

num = [1,21,3,4,5,35,5,4,3,5,98,21,14,17,32]
num= [40,30,30,50]

def sol(num, ans):
    num.sort()
    if len(num) == 1:
        return ans
    elif len(num) == 2:
        return ans+sum(num)
    else:
        ans += (num[0]+num[1])
        num = [num[0]+num[1]]+num[2:]
        return sol(num, ans)