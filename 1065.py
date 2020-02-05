n =  input()

def sol(n):
    num = str(n)
    dif = int(num[0])-int(num[1])

    val = 2
    while(val<len(num)):
        if int(num[val-1])-int(num[val]) != dif:
            break
        else:
            val += 1
    
    if val == len(num):
        return True


def fin(n):

    final = []

    for i in range(100,n+1):
        if sol(i) == True:
            final.append(i)

    if n < 99:
        print(n)
        return n
    else:
        print(99+len(final))
        return 99+len(final)

fin(n)