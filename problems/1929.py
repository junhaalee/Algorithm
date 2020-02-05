s,f = map(int, input().split())

for i in range(s, f+1):

    k = 2

    while(True):
        if i == 1 or i == k or i%k == 0 or k*k >= i:
            break
        else:
            k+=1
    
    if k == i:
        print(i)

