n = int(input())

panel = [input() for _ in range(n)]

def check(temp):
    str_temp = []
    for i in range(len(temp)):
        str_temp += list(temp[i])
    if len(set(str_temp)) == 1:
        return True
    else:
        return False


def sol(x, y, n):

    temp = [panel[y][x:x+n] for y in range(y,y+n)]

    if check(temp) == True:
        print(temp[0][0],end='')
    else:
        print('(',end='')
        sol(x,y,n//2)
        sol(x+n//2,y,n//2)
        sol(x,y+n//2,n//2)
        sol(x+n//2,y+n//2,n//2)
        print(')',end='')

sol(0,0,n)