import sys
input = sys.stdin.readline

ind = 1
while True:

    l,p,v = map(int, input().split())
    
    if l:
        n,k = v//p, v%p
        ans = n*l + min([k,l])
        print('Case '+str(ind)+': '+str(ans))
        ind += 1
    else:
        break